/** @mierp-module **/

import miViewAnalysis from "@mi_dashboard/js/component/main/mi_view_analysis";
import miConfigAnalysis from "@mi_dashboard/js/component/main/mi_config_analysis";
import { useService } from "@web/core/utils/hooks";
import { Component, useRef, onRendered, onPatched, onMounted } from "@mierp/owl";
export class miAnalysisController extends Component {
    setup() {
        self = this;
        self.action = useService('action');
        self.container = useRef('miAnalysisContainer');
        self.context = false;
        if (self.props && self.props.context) {
            self.context = self.props.context;
        };
        // self.render();
        onPatched(() => {
            self = this;
        });
        onMounted(() => {
            self = this;
            self.$el = $(self.container.el);
            console.log('onMounted', self.props.value);
            var $viewAnalysis = new miViewAnalysis(self);
            var $configAnalysis = new miConfigAnalysis(self, $viewAnalysis);
            $configAnalysis.appendTo(self.$el);
            $viewAnalysis.appendTo(self.$el);
            self.$viewAnalysis = $viewAnalysis;
            self.$configAnalysis = $configAnalysis;
        });
    }
}

miAnalysisController.template = "miAnalysis";