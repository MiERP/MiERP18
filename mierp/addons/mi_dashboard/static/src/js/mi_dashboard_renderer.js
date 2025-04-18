mierp.define('mi_dashboard.miDashboardRenderer', function (require) {
    "use strict";
    
    var AbstractRenderer = require('web.AbstractRenderer');
    var miViewDashboard = require('mi_dashboard.miViewDashboard');
    var miConfigDashboard = require('mi_dashboard.miConfigDashboard');
    return AbstractRenderer.extend({
        template: "miDashboard",
        events: _.extend({}, AbstractRenderer.prototype.events, {
        }),
        init: function (parent, state, params) {
            var self = this;
            this._super.apply(this, arguments);
            // console.log("Init App Renderer", this, parent, state, params);
            self.parent = parent;
            if (parent.props) self.props = parent.props;
            // Define Global Variables
        },
        start: function () {
            var self = this;
            // console.log("Start App Renderer");

            // Dashboard Component
            var $viewDashboard = new miViewDashboard(self);
            var $configDashboard = new miConfigDashboard(self, $viewDashboard);
            $configDashboard.appendTo(self.$el);
            $viewDashboard.appendTo(self.$el);
        },
        destroy: function() {
            // console.log("Destroy App Renderer");
            this._super.apply(this, arguments);
        },
    });

});
