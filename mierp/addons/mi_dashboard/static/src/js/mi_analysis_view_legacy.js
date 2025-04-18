mierp.define('mi_dashboard.miAnalysisView', function (require) {
    "use strict";
    
    var core = require('web.core');
    var AbstractView = require('web.AbstractView');
    var view_registry = require('web.view_registry');
    var _lt = core._lt;
    var miAnalysisModel = require('mi_dashboard.miAnalysisModel');
    var miAnalysisController = require('mi_dashboard.miAnalysisController');
    var miAnalysisRenderer = require('mi_dashboard.miAnalysisRenderer');
    var miAnalysisView = AbstractView.extend({
        template: "miAnalysis",
        display_name: _lt('miAnalysis'),
        events: {
        },
        icon: 'fa-tachometer',
        config: _.extend({},AbstractView.prototype.config, {
            Model: miAnalysisModel,
            Controller: miAnalysisController,
            Renderer: miAnalysisRenderer,
        }),
        viewType: 'mianalysis',
        withControlPanel: false,
        withSearchPanel: false,
    
        init: function () {
            this._super.apply(this, arguments);
        },
    });
    
    view_registry.add('mianalysis', miAnalysisView);
    
    return miAnalysisView;
});