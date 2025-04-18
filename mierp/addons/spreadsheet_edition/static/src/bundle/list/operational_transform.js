/** @mierp-module */

import * as spreadsheet from "@mierp/o-spreadsheet";
const { otRegistry } = spreadsheet.registries;

otRegistry
    .addTransformation(
        "INSERT_mierp_LIST",
        ["INSERT_mierp_LIST", "DUPLICATE_mierp_LIST"],
        transformNewListCommand
    )
    .addTransformation(
        "DUPLICATE_mierp_LIST",
        ["INSERT_mierp_LIST", "DUPLICATE_mierp_LIST"],
        transformNewListCommand
    )
    .addTransformation(
        "REMOVE_mierp_LIST",
        ["RENAME_mierp_LIST", "UPDATE_mierp_LIST_DOMAIN", "UPDATE_mierp_LIST"],
        (toTransform, executed) => {
            if (toTransform.listId === executed.listId) {
                return undefined;
            }
            return toTransform;
        }
    )
    .addTransformation(
        "REMOVE_mierp_LIST",
        ["RE_INSERT_mierp_LIST", "DUPLICATE_mierp_LIST"],
        (toTransform, executed) => {
            if (toTransform.id === executed.listId) {
                return undefined;
            }
            return toTransform;
        }
    );

function transformNewListCommand(toTransform) {
    const idKey = "newListId" in toTransform ? "newListId" : "id";
    return {
        ...toTransform,
        [idKey]: (parseInt(toTransform[idKey], 10) + 1).toString(),
    };
}
