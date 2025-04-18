/** @mierp-module */

import { mierpCorePlugin } from "@spreadsheet/plugins";
import { coreTypes, helpers } from "@mierp/o-spreadsheet";
import { omit } from "@web/core/utils/objects";
const { deepEquals } = helpers;

/** Plugin that link charts with mierp menus. It can contain either the Id of the mierp menu, or its xml id. */
export class ChartmierpMenuPlugin extends mierpCorePlugin {
    static getters = /** @type {const} */ (["getChartmierpMenu"]);
    constructor(config) {
        super(config);
        this.mierpMenuReference = {};
    }

    /**
     * Handle a spreadsheet command
     * @param {Object} cmd Command
     */
    handle(cmd) {
        switch (cmd.type) {
            case "LINK_mierp_MENU_TO_CHART":
                this.history.update("mierpMenuReference", cmd.chartId, cmd.mierpMenuId);
                break;
            case "DELETE_FIGURE":
                this.history.update("mierpMenuReference", cmd.id, undefined);
                break;
            case "DUPLICATE_SHEET":
                this.updateOnDuplicateSheet(cmd.sheetId, cmd.sheetIdTo);
                break;
        }
    }

    updateOnDuplicateSheet(sheetIdFrom, sheetIdTo) {
        for (const oldChartId of this.getters.getChartIds(sheetIdFrom)) {
            if (!this.mierpMenuReference[oldChartId]) {
                continue;
            }
            const oldChartDefinition = this.getters.getChartDefinition(oldChartId);
            const oldFigure = this.getters.getFigure(sheetIdFrom, oldChartId);
            const newChartId = this.getters.getChartIds(sheetIdTo).find((newChartId) => {
                const newChartDefinition = this.getters.getChartDefinition(newChartId);
                const newFigure = this.getters.getFigure(sheetIdTo, newChartId);
                return (
                    deepEquals(oldChartDefinition, newChartDefinition) &&
                    deepEquals(omit(newFigure, "id"), omit(oldFigure, "id")) // compare size and position
                );
            });

            if (newChartId) {
                this.history.update(
                    "mierpMenuReference",
                    newChartId,
                    this.mierpMenuReference[oldChartId]
                );
            }
        }
    }

    /**
     * Get mierp menu linked to the chart
     *
     * @param {string} chartId
     * @returns {object | undefined}
     */
    getChartmierpMenu(chartId) {
        const menuId = this.mierpMenuReference[chartId];
        return menuId ? this.getters.getIrMenu(menuId) : undefined;
    }

    import(data) {
        if (data.chartmierpMenusReferences) {
            this.mierpMenuReference = data.chartmierpMenusReferences;
        }
    }

    export(data) {
        data.chartmierpMenusReferences = this.mierpMenuReference;
    }
}

coreTypes.add("LINK_mierp_MENU_TO_CHART");
