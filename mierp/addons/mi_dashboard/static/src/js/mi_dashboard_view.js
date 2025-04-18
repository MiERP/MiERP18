/** @mierp-module **/

import { registry } from "@web/core/registry";
import { miDashboardController } from "@mi_dashboard/js/mi_dashboard_controller";

export const miDashboardView = {
    type: "midashboard",
    display_name: "miDashboard",
    icon: "fa-tachometer",
    multiRecord: true,
    Controller: miDashboardController,
};

registry.category("views").add("midashboard", miDashboardView);