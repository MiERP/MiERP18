/** @mierp-module **/

import { registry } from "@web/core/registry";
import miViewVisual from "@mi_dashboard/js/component/main/mi_view_visual";
import { Component, useRef, onRendered, onPatched, onMounted } from "@mierp/owl";
class miAnalysisWidget extends Component {
    setup() {
        self = this;
        self.widgetContainer = useRef('widgetContainer');
        // self.render();
        onPatched(() => {
            self = this;
            console.log('onPatched', self.props.record.data);
            self.analysis_data = self.props.record.data[self.props.name];
            if (self.widgetContainer && self.widgetContainer.el && self.analysis_data) {
                var $el = $(self.widgetContainer.el);
                $el.empty();
                self.$visual = new miViewVisual(self, {
                    analysis_data: JSON.parse(self.analysis_data),
                });
                self.$visual.appendTo($el);
            }
        });
        onMounted(() => {
            self = this;
            console.log('onRendered', self.props.record.data);
            self.analysis_data = self.props.record.data[self.props.name];
            if (self.widgetContainer && self.widgetContainer.el && self.analysis_data) {
                var $el = $(self.widgetContainer.el);
                $el.empty();
                self.$visual = new miViewVisual(self, {
                    analysis_data: JSON.parse(self.analysis_data),
                });
                self.$visual.appendTo($el);
            }
        });
    }
}
miAnalysisWidget.template = 'mi_dashboard.miAnalysisWidget';

export const miAnalysisField = {
    component: miAnalysisWidget,
    supportedTypes: ["text"],
};
registry.category("fields").add("mi_analysis", miAnalysisField);