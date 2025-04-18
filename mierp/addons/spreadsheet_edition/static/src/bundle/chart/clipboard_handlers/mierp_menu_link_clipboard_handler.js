import { AbstractFigureClipboardHandler, registries } from "@mierp/o-spreadsheet";
const { clipboardHandlersRegistries } = registries;

class mierpLinkClipboardHandler extends AbstractFigureClipboardHandler {
    copy(data) {
        const sheetId = this.getters.getActiveSheetId();
        const figure = this.getters.getFigure(sheetId, data.figureId);
        if (!figure) {
            throw new Error(`No figure for the given id: ${data.figureId}`);
        }
        if (figure.tag !== "chart") {
            return;
        }
        const mierpMenuId = this.getters.getChartmierpMenu(data.figureId);
        if (mierpMenuId) {
            return { mierpMenuId };
        }
    }
    paste(target, clippedContent, options) {
        if (!target.figureId || !clippedContent.mierpMenuId) {
            return;
        }
        const { figureId } = target;
        const { mierpMenuId } = clippedContent;
        this.dispatch("LINK_mierp_MENU_TO_CHART", {
            chartId: figureId,
            mierpMenuId: mierpMenuId.xmlid || mierpMenuId.id,
        });
    }
}

clipboardHandlersRegistries.figureHandlers.add("mierp_menu_link", mierpLinkClipboardHandler);
