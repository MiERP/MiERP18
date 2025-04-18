/** @mierp-module */
// @ts-check

import { helpers } from "@mierp/o-spreadsheet";

const { getFunctionsFromTokens } = helpers;

/** @typedef {import("@mierp/o-spreadsheet").Token} Token */

/**
 * Parse a spreadsheet formula and detect the number of LIST functions that are
 * present in the given formula.
 *
 * @param {Token[]} tokens
 *
 * @returns {number}
 */
export function getNumberOfListFormulas(tokens) {
    return getFunctionsFromTokens(tokens, ["mierp.LIST", "mierp.LIST.HEADER"]).length;
}

/**
 * Get the first List function description of the given formula.
 *
 * @param {Token[]} tokens
 *
 * @returns {import("../helpers/mierp_functions_helpers").mierpFunctionDescription|undefined}
 */
export function getFirstListFunction(tokens) {
    return getFunctionsFromTokens(tokens, ["mierp.LIST", "mierp.LIST.HEADER"])[0];
}
