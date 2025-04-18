import { components } from "@mierp/o-spreadsheet";
import { mierp_AGGREGATORS } from "@spreadsheet/pivot/pivot_helpers";
const { PivotLayoutConfigurator } = components;

export class mierpPivotLayoutConfigurator extends PivotLayoutConfigurator {
    setup() {
        super.setup(...arguments);
        this.AGGREGATORS = mierp_AGGREGATORS;
    }
}
