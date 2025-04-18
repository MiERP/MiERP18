/** @mierp-module */

import { CommonmierpChartConfigPanel } from "../common/config_panel";
import { components } from "@mierp/o-spreadsheet";

const { Checkbox } = components;

export class mierpLineChartConfigPanel extends CommonmierpChartConfigPanel {
    static template = "spreadsheet_edition.mierpLineChartConfigPanel";
    static components = {
        ...CommonmierpChartConfigPanel.components,
        Checkbox,
    };

    onUpdateStacked(stacked) {
        this.props.updateChart(this.props.figureId, {
            stacked,
        });
    }
    onUpdateCumulative(cumulative) {
        this.props.updateChart(this.props.figureId, {
            cumulative,
        });
    }
}
