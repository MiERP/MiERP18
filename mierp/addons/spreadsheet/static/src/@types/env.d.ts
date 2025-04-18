import { SpreadsheetChildEnv as SSChildEnv } from "@mierp/o-spreadsheet";
import { Services } from "services";

declare module "@spreadsheet" {
    import { Model } from "@mierp/o-spreadsheet";

    export interface SpreadsheetChildEnv extends SSChildEnv {
        model: mierpSpreadsheetModel;
        services: Services;
    }
}
