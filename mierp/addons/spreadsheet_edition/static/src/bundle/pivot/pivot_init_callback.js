/** @mierp-module **/
//@ts-check

import { helpers, stores } from "@mierp/o-spreadsheet";
import { mierpPivot } from "@spreadsheet/pivot/mierp_pivot";
import { Domain } from "@web/core/domain";
import { deepCopy } from "@web/core/utils/objects";
import { _t } from "@web/core/l10n/translation";

const uuidGenerator = new helpers.UuidGenerator();
const { parseDimension, isDateOrDatetimeField } = helpers;

const { SidePanelStore } = stores;

/**
 * Asserts that the given result is successful, otherwise throws an error.
 *
 * @param {import("@mierp/o-spreadsheet").DispatchResult} result
 */
function ensureSuccess(result) {
    if (!result.isSuccessful) {
        throw new Error(`Couldn't insert pivot in spreadsheet. Reasons : ${result.reasons}`);
    }
}

function addEmptyGranularity(dimensions, fields) {
    return dimensions.map((dimension) => {
        if (isDateOrDatetimeField(fields[dimension.fieldName])) {
            return {
                granularity: "month",
                ...dimension,
            };
        }
        return dimension;
    });
}

export function insertPivot(pivotData) {
    const fields = pivotData.metaData.fields;
    const measures = pivotData.metaData.activeMeasures.map((measure) => ({
        id: fields[measure]?.aggregator ? `${measure}:${fields[measure].aggregator}` : measure,
        fieldName: measure,
        aggregator: fields[measure]?.aggregator,
    }));
    /** @type {import("@spreadsheet").mierpPivotCoreDefinition} */
    const pivot = deepCopy({
        type: "mierp",
        domain: new Domain(pivotData.searchParams.domain).toJson(),
        context: pivotData.searchParams.context,
        sortedColumn: pivotData.metaData.sortedColumn,
        measures,
        model: pivotData.metaData.resModel,
        columns: addEmptyGranularity(
            pivotData.metaData.fullColGroupBys.map(parseDimension),
            fields
        ),
        rows: addEmptyGranularity(pivotData.metaData.fullRowGroupBys.map(parseDimension), fields),
        name: pivotData.name,
        actionXmlId: pivotData.actionXmlId,
    });
    /**
     * @param {import("@spreadsheet").mierpSpreadsheetModel} model
     */
    return async (model, stores) => {
        const pivotId = uuidGenerator.uuidv4();
        ensureSuccess(
            model.dispatch("ADD_PIVOT", {
                pivotId,
                pivot,
            })
        );
        const ds = model.getters.getPivot(pivotId);
        if (!(ds instanceof mierpPivot)) {
            throw new Error("The pivot data source is not an mierpPivot");
        }
        await ds.load();

        let sheetName = _t("%(pivot_name)s (Pivot #%(pivot_id)s)", {
            pivot_name: pivot.name,
            pivot_id: model.getters.getPivotFormulaId(pivotId),
        });
        // Add an empty sheet in the case of an existing spreadsheet.
        if (!this.isEmptySpreadsheet) {
            const sheetId = uuidGenerator.uuidv4();
            const sheetIdFrom = model.getters.getActiveSheetId();
            if (model.getters.getSheetIdByName(sheetName)) {
                sheetName = undefined;
            }
            model.dispatch("CREATE_SHEET", {
                sheetId,
                position: model.getters.getSheetIds().length,
                name: sheetName,
            });
            model.dispatch("ACTIVATE_SHEET", { sheetIdFrom, sheetIdTo: sheetId });
        } else {
            model.dispatch("RENAME_SHEET", {
                sheetId: model.getters.getActiveSheetId(),
                name: sheetName,
            });
        }
        const sheetId = model.getters.getActiveSheetId();

        const table = ds.getTableStructure();
        ensureSuccess(
            model.dispatch("INSERT_PIVOT_WITH_TABLE", {
                sheetId,
                col: 0,
                row: 0,
                pivotId,
                table: table.export(),
                pivotMode: "static",
            })
        );

        const columns = [];
        for (let col = 0; col <= table.columns[table.columns.length - 1].length; col++) {
            columns.push(col);
        }
        model.dispatch("AUTORESIZE_COLUMNS", { sheetId, cols: columns });
        const sidePanel = stores.get(SidePanelStore);
        sidePanel.open("PivotSidePanel", { pivotId });
    };
}
