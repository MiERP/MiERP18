/** @mierp-module **/

import miViewDashboard from "@mi_dashboard/js/component/main/mi_view_dashboard";
import miConfigDashboard from "@mi_dashboard/js/component/main/mi_config_dashboard";
import { useService } from "@web/core/utils/hooks";
import { Component, useRef, onRendered, onPatched, onMounted } from "@mierp/owl";
export class miDashboardController extends Component {
    setup() {
        self = this;
        self.action = useService('action');
        self.container = useRef('miDashboardContainer');
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
            var $viewDashboard = new miViewDashboard(self);
            var $configDashboard = new miConfigDashboard(self, $viewDashboard);
            $configDashboard.appendTo(self.$el);
            $viewDashboard.appendTo(self.$el);
            self.$viewDashboard = $viewDashboard;
            self.$configDashboard = $configDashboard;
        });
    }


}

miDashboardController.template = "miDashboard";