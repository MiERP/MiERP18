/** @mierp-module */

import { CorePlugin, UIPlugin } from "@mierp/o-spreadsheet";

/**
 * An o-spreadsheet core plugin with access to all custom mierp plugins
 * @type {import("@spreadsheet").mierpCorePluginConstructor}
 **/
export const mierpCorePlugin = CorePlugin;

/**
 * An o-spreadsheet UI plugin with access to all custom mierp plugins
 * @type {import("@spreadsheet").mierpUIPluginConstructor}
 **/
export const mierpUIPlugin = UIPlugin;
