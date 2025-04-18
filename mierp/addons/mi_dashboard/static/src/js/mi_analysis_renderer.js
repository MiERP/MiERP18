mierp.define('mi_dashboard.miAnalysisRenderer', function (require) {
    "use strict";
    
    var AbstractRenderer = require('web.AbstractRenderer');
    var miViewAnalysis = require('mi_dashboard.miViewAnalysis');
    var miConfigAnalysis = require('mi_dashboard.miConfigAnalysis');
    return AbstractRenderer.extend({
        template: "miAnalysis",
        events: _.extend({}, AbstractRenderer.prototype.events, {
        }),
        init: function (parent, state, params) {
            var self = this;
            this._super.apply(this, arguments);
            // console.log("Init App Renderer", this, parent, state, params);
            self.parent = parent;
            if (parent.props) self.props = parent.props;
        },
        start: function () {
            var self = this;
            // console.log("Start App Renderer");

            // Dashboard Component
            var $viewAnalysis = new miViewAnalysis(self);
            self.$viewAnalysis = $viewAnalysis;
            // Analysis Component
            var $configAnalysis = new miConfigAnalysis(self, $viewAnalysis);
            self.$configAnalysis = $configAnalysis;

            // Append
            $configAnalysis.appendTo(self.$el);
            $viewAnalysis.appendTo(self.$el);
        },
        destroy: function() {
            // console.log("Destroy App Renderer");
            this._super.apply(this, arguments);
        },
    });

});
