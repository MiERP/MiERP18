declare module "@spreadsheet" {
    import { Model } from "@mierp/o-spreadsheet";

    export interface mierpSpreadsheetModel extends Model {
        getters: mierpGetters;
        dispatch: mierpDispatch;
    }

    export interface mierpSpreadsheetModelConstructor {
        new (
            data: object,
            config: Partial<Model["config"]>,
            revisions: object[]
        ): mierpSpreadsheetModel;
    }
}
