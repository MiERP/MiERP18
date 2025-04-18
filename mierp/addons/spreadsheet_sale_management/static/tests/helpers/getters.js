import { helpers } from "@mierp/o-spreadsheet";

const { toCartesian } = helpers;

export function getFieldSync(model, xc, sheetId = model.getters.getActiveSheetId()) {
    return model.getters.getFieldSync({ ...toCartesian(xc), sheetId });
}
