/** @mierp-module **/
// @ts-check

import { helpers } from "@mierp/o-spreadsheet";

const { getFunctionsFromTokens } = helpers;

/**
 * @typedef {import("@mierp/o-spreadsheet").Token} Token
 * @typedef  {import("@spreadsheet/helpers/mierp_functions_helpers").mierpFunctionDescription} mierpFunctionDescription
 */

/**
 * @param {Token[]} tokens
 * @returns {number}
 */
export function getNumberOfAccountFormulas(tokens) {
    return getFunctionsFromTokens(tokens, ["mierp.BALANCE", "mierp.CREDIT", "mierp.DEBIT"]).length;
}

/**
 * Get the first Account function description of the given formula.
 *
 * @param {Token[]} tokens
 * @returns {mierpFunctionDescription | undefined}
 */
export function getFirstAccountFunction(tokens) {
    return getFunctionsFromTokens(tokens, ["mierp.BALANCE", "mierp.CREDIT", "mierp.DEBIT"])[0];
}
