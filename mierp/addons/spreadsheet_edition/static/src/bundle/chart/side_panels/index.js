/** @mierp-module */

import * as spreadsheet from "@mierp/o-spreadsheet";
import { CommonmierpChartConfigPanel } from "./common/config_panel";
import { mierpBarChartConfigPanel } from "./mierp_bar/mierp_bar_config_panel";
import { mierpLineChartConfigPanel } from "./mierp_line/mierp_line_config_panel";
import { mierpChartWithAxisDesignPanel } from "./mierp_chart_with_axis/design_panel";
import { _t } from "@web/core/l10n/translation";

const { chartSidePanelComponentRegistry, chartSubtypeRegistry } = spreadsheet.registries;
const { PieChartDesignPanel } = spreadsheet.components;

chartSidePanelComponentRegistry
    .add("mierp_line", {
        configuration: mierpLineChartConfigPanel,
        design: mierpChartWithAxisDesignPanel,
    })
    .add("mierp_bar", {
        configuration: mierpBarChartConfigPanel,
        design: mierpChartWithAxisDesignPanel,
    })
    .add("mierp_pie", {
        configuration: CommonmierpChartConfigPanel,
        design: PieChartDesignPanel,
    });

chartSubtypeRegistry.add("mierp_line", {
    matcher: (definition) =>
        definition.type === "mierp_line" && !definition.stacked && !definition.fillArea,
    subtypeDefinition: { stacked: false, fillArea: false },
    displayName: _t("Line"),
    chartSubtype: "mierp_line",
    chartType: "mierp_line",
    category: "line",
    preview: "o-spreadsheet-ChartPreview.LINE_CHART",
});
chartSubtypeRegistry.add("mierp_stacked_line", {
    matcher: (definition) =>
        definition.type === "mierp_line" && definition.stacked && !definition.fillArea,
    subtypeDefinition: { stacked: true, fillArea: false },
    displayName: _t("Stacked Line"),
    chartSubtype: "mierp_stacked_line",
    chartType: "mierp_line",
    category: "line",
    preview: "o-spreadsheet-ChartPreview.STACKED_LINE_CHART",
});
chartSubtypeRegistry.add("mierp_area", {
    matcher: (definition) =>
        definition.type === "mierp_line" && !definition.stacked && definition.fillArea,
    subtypeDefinition: { stacked: false, fillArea: true },
    displayName: _t("Area"),
    chartSubtype: "mierp_area",
    chartType: "mierp_line",
    category: "area",
    preview: "o-spreadsheet-ChartPreview.AREA_CHART",
});
chartSubtypeRegistry.add("mierp_stacked_area", {
    matcher: (definition) =>
        definition.type === "mierp_line" && definition.stacked && definition.fillArea,
    subtypeDefinition: { stacked: true, fillArea: true },
    displayName: _t("Stacked Area"),
    chartSubtype: "mierp_stacked_area",
    chartType: "mierp_line",
    category: "area",
    preview: "o-spreadsheet-ChartPreview.STACKED_AREA_CHART",
});
chartSubtypeRegistry.add("mierp_bar", {
    matcher: (definition) => definition.type === "mierp_bar" && !definition.stacked,
    subtypeDefinition: { stacked: false },
    displayName: _t("Column"),
    chartSubtype: "mierp_bar",
    chartType: "mierp_bar",
    category: "column",
    preview: "o-spreadsheet-ChartPreview.COLUMN_CHART",
});
chartSubtypeRegistry.add("mierp_stacked_bar", {
    matcher: (definition) => definition.type === "mierp_bar" && definition.stacked,
    subtypeDefinition: { stacked: true },
    displayName: _t("Stacked Column"),
    chartSubtype: "mierp_stacked_bar",
    chartType: "mierp_bar",
    category: "column",
    preview: "o-spreadsheet-ChartPreview.STACKED_COLUMN_CHART",
});
chartSubtypeRegistry.add("mierp_pie", {
    displayName: _t("Pie"),
    chartSubtype: "mierp_pie",
    chartType: "mierp_pie",
    category: "pie",
    preview: "o-spreadsheet-ChartPreview.PIE_CHART",
});
