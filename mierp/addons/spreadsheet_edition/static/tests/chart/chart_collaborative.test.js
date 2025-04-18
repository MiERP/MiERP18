import { beforeEach, describe, test } from "@mierp/hoot";
import { createBasicChart } from "@spreadsheet/../tests/helpers/commands";
import { defineSpreadsheetModels, getBasicServerData } from "@spreadsheet/../tests/helpers/data";
import {
    setupCollaborativeEnv,
    spExpect,
} from "@spreadsheet_edition/../tests/helpers/collaborative_helpers";

describe.current.tags("headless");
defineSpreadsheetModels();

/** @typedef {import("@spreadsheet/o_spreadsheet/o_spreadsheet").Model} Model */

let alice, bob, charlie, network;

beforeEach(async () => {
    ({ alice, bob, charlie, network } = await setupCollaborativeEnv(getBasicServerData()));
});

test("Chart link to mierp menu collaborative", async () => {
    const chartId = "1";
    const sheetId = alice.getters.getActiveSheetId();
    createBasicChart(alice, chartId);
    await network.concurrent(() => {
        alice.dispatch("DELETE_FIGURE", { id: chartId, sheetId });
        bob.dispatch("LINK_mierp_MENU_TO_CHART", {
            chartId,
            mierpMenuId: "mierpTestMenu",
        });
    });
    spExpect([alice, bob, charlie]).toHaveSynchronizedValue(
        (user) => user.getters.getFigures(sheetId),
        []
    );
    spExpect([alice, bob, charlie]).toHaveSynchronizedValue(
        (user) => user.getters.getChartmierpMenu(chartId),
        undefined
    );
});
