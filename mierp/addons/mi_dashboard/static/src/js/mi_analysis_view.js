/** @mierp-module **/

import { registry } from "@web/core/registry";
import { miAnalysisController } from "@mi_dashboard/js/mi_analysis_controller";

export const miAnalysisView = {
    type: "mianalysis",
    display_name: "miAnalysis",
    icon: "fa-tachometer",
    multiRecord: true,
    Controller: miAnalysisController,
};

registry.category("views").add("mianalysis", miAnalysisView);