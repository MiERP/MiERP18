/** @mierp-module **/

import { patch } from "@web/core/utils/patch";
import * as spreadsheet from "@mierp/o-spreadsheet";
import { IrMenuSelector } from "@spreadsheet_edition/bundle/ir_menu_selector/ir_menu_selector";

const { GenericChartConfigPanel, ScorecardChartConfigPanel, GaugeChartConfigPanel, Section } =
    spreadsheet.components;

/**
 * Patch the chart configuration panel to add an input to
 * link the chart to an mierp menu.
 */
function patchChartPanelWithMenu(PanelComponent) {
    patch(PanelComponent.prototype, {
        get mierpMenuId() {
            const menu = this.env.model.getters.getChartmierpMenu(this.props.figureId);
            return menu ? menu.id : undefined;
        },
        /**
         * @param {number | undefined} mierpMenuId
         */
        updatemierpLink(mierpMenuId) {
            if (!mierpMenuId) {
                this.env.model.dispatch("LINK_mierp_MENU_TO_CHART", {
                    chartId: this.props.figureId,
                    mierpMenuId: undefined,
                });
                return;
            }
            const menu = this.env.model.getters.getIrMenu(mierpMenuId);
            this.env.model.dispatch("LINK_mierp_MENU_TO_CHART", {
                chartId: this.props.figureId,
                mierpMenuId: menu.xmlid || menu.id,
            });
        },
    });
    PanelComponent.components = {
        ...PanelComponent.components,
        IrMenuSelector,
        Section,
    };
}
patchChartPanelWithMenu(GenericChartConfigPanel);
patchChartPanelWithMenu(GaugeChartConfigPanel);
patchChartPanelWithMenu(ScorecardChartConfigPanel);
