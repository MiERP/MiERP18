import { globalFiltersFieldMatchers } from "@spreadsheet/global_filters/plugins/global_filters_core_plugin";

import { AbstractFigureClipboardHandler, registries } from "@mierp/o-spreadsheet";

const { clipboardHandlersRegistries } = registries;

class mierpChartFieldMatchingClipboardHandler extends AbstractFigureClipboardHandler {
    copy({ figureId }) {
        if (!this.getters.getChart(figureId)?.type.startsWith("mierp")) {
            return;
        }
        return {
            mierpChartFieldMatching: this.getters.getChartFieldMatch(figureId),
        };
    }

    paste(target, clippedContent, options) {
        const { figureId: newFigureId } = target;
        const clippedMatchings = clippedContent.mierpChartFieldMatching;
        if (!clippedMatchings) {
            return;
        }

        const mierpChartIds = globalFiltersFieldMatchers["chart"].getIds();
        for (const filterId in clippedMatchings) {
            const copiedFieldMatching = clippedMatchings[filterId];
            const filter = this.getters.getGlobalFilter(filterId);
            const currentChartMatchings = {};
            // copy existing matching of other chars for this filter
            for (const chartId of mierpChartIds) {
                currentChartMatchings[chartId] = this.getters.getmierpChartFieldMatching(
                    chartId,
                    filterId
                );
            }
            if (options?.isCutOperation) {
                delete currentChartMatchings[clippedContent.figureId];
            }
            if (copiedFieldMatching.chain === currentChartMatchings[newFigureId]?.chain) {
                // avoid dispatching a command if the automatic field matching already set
                // the same matching
                continue;
            }
            currentChartMatchings[newFigureId] = copiedFieldMatching;
            this.dispatch("EDIT_GLOBAL_FILTER", {
                filter,
                chart: currentChartMatchings,
            });
        }
    }
}

clipboardHandlersRegistries.figureHandlers.add(
    "mierp_chart_field_matching",
    mierpChartFieldMatchingClipboardHandler
);
