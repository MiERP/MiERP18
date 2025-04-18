/** @mierp-module */

import * as spreadsheet from "@mierp/o-spreadsheet";
import { mierpPivot } from "@spreadsheet/pivot/mierp_pivot";
import { patch } from "@web/core/utils/patch";
const { helpers } = spreadsheet;
const { formatValue } = helpers;

/**
 * @typedef {import("@mierp/o-spreadsheet").PivotDomain} PivotDomain
 */

patch(mierpPivot.prototype, {
    /**
     * High level method computing the formatted result of PIVOT.HEADER functions.
     *
     * @param {PivotDomain} domain
     */
    getPivotHeaderFormattedValue(domain) {
        const { value, format } = this.getPivotHeaderValueAndFormat(domain);
        if (typeof value === "string") {
            return value;
        }
        const locale = this.getters.getLocale();
        return formatValue(value, { format, locale });
    },
});
