/** @mierp-module */

import * as spreadsheet from "@mierp/o-spreadsheet";

const { chartComponentRegistry } = spreadsheet.registries;
const { ChartJsComponent } = spreadsheet.components;

chartComponentRegistry.add("mierp_bar", ChartJsComponent);
chartComponentRegistry.add("mierp_line", ChartJsComponent);
chartComponentRegistry.add("mierp_pie", ChartJsComponent);

import { mierpChartCorePlugin } from "./plugins/mierp_chart_core_plugin";
import { ChartmierpMenuPlugin } from "./plugins/chart_mierp_menu_plugin";
import { mierpChartUIPlugin } from "./plugins/mierp_chart_ui_plugin";

export { mierpChartCorePlugin, ChartmierpMenuPlugin, mierpChartUIPlugin };
