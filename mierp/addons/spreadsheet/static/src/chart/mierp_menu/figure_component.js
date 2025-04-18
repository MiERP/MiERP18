/** @mierp-module **/

import { patch } from "@web/core/utils/patch";
import * as spreadsheet from "@mierp/o-spreadsheet";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";

patch(spreadsheet.components.FigureComponent.prototype, {
    setup() {
        super.setup();
        this.menuService = useService("menu");
        this.actionService = useService("action");
        this.notificationService = useService("notification");
    },
    async navigateTomierpMenu() {
        const menu = this.env.model.getters.getChartmierpMenu(this.props.figure.id);
        if (!menu) {
            throw new Error(`Cannot find any menu associated with the chart`);
        }
        if (!menu.actionID) {
            this.notificationService.add(
                _t(
                    "The menu linked to this chart doesn't have an corresponding action. Please link the chart to another menu."
                ),
                { type: "danger" }
            );
            return;
        }
        await this.actionService.doAction(menu.actionID);
    },
    get hasmierpMenu() {
        return this.env.model.getters.getChartmierpMenu(this.props.figure.id) !== undefined;
    },
    async onClick() {
        if (this.env.isDashboard() && this.hasmierpMenu) {
            this.navigateTomierpMenu();
        }
    },
});
