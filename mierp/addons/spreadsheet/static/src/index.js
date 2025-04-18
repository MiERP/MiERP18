/** @mierp-module */

/**
 * This file is meant to load the different subparts of the module
 * to guarantee their plugins are loaded in the right order
 *
 * dependency:
 *             other plugins
 *                   |
 *                  ...
 *                   |
 *                filters
 *                /\    \
 *               /  \    \
 *           pivot  list  mierp chart
 */

/** TODO: Introduce a position parameter to the plugin registry in order to load them in a specific order */
import * as spreadsheet from "@mierp/o-spreadsheet";
const { corePluginRegistry, coreViewsPluginRegistry } = spreadsheet.registries;

import { GlobalFiltersCorePlugin, GlobalFiltersUIPlugin } from "@spreadsheet/global_filters/index";
import { PivotmierpCorePlugin, PivotUIGlobalFilterPlugin } from "@spreadsheet/pivot/index"; // list depends on filter for its getters
import { ListCorePlugin, ListUIPlugin } from "@spreadsheet/list/index"; // pivot depends on filter for its getters
import {
    ChartmierpMenuPlugin,
    mierpChartCorePlugin,
    mierpChartUIPlugin,
} from "@spreadsheet/chart/index"; // mierpchart depends on filter for its getters
import { PivotCoreGlobalFilterPlugin } from "./pivot/plugins/pivot_core_global_filter_plugin";
import { PivotmierpUIPlugin } from "./pivot/plugins/pivot_mierp_ui_plugin";

corePluginRegistry.add("mierpGlobalFiltersCorePlugin", GlobalFiltersCorePlugin);
corePluginRegistry.add("PivotmierpCorePlugin", PivotmierpCorePlugin);
corePluginRegistry.add("mierpPivotGlobalFiltersCorePlugin", PivotCoreGlobalFilterPlugin);
corePluginRegistry.add("mierpListCorePlugin", ListCorePlugin);
corePluginRegistry.add("mierpChartCorePlugin", mierpChartCorePlugin);
corePluginRegistry.add("chartmierpMenuPlugin", ChartmierpMenuPlugin);

coreViewsPluginRegistry.add("mierpGlobalFiltersUIPlugin", GlobalFiltersUIPlugin);
coreViewsPluginRegistry.add("mierpPivotGlobalFilterUIPlugin", PivotUIGlobalFilterPlugin);
coreViewsPluginRegistry.add("mierpListUIPlugin", ListUIPlugin);
coreViewsPluginRegistry.add("mierpChartUIPlugin", mierpChartUIPlugin);
coreViewsPluginRegistry.add("mierpPivotUIPlugin", PivotmierpUIPlugin);
