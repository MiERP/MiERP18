mierp.define('mi_dashboard.miDashboardView', function (require) {
    "use strict";
    
    var core = require('web.core');
    var AbstractView = require('web.AbstractView');
    var view_registry = require('web.view_registry');
    var _lt = core._lt;
    var miDashboardModel = require('mi_dashboard.miDashboardModel');
    var miDashboardController = require('mi_dashboard.miDashboardController');
    var miDashboardRenderer = require('mi_dashboard.miDashboardRenderer');
    var miDashboardView = AbstractView.extend({
        template: "miDashboard",
        display_name: _lt('miDashboard'),
        events: {
        },
        icon: 'fa-tachometer',
        config: _.extend({},AbstractView.prototype.config, {
            Model: miDashboardModel,
            Controller: miDashboardController,
            Renderer: miDashboardRenderer,
        }),
        viewType: 'midashboard',
        withControlPanel: false,
        withSearchPanel: false,
    
        init: function () {
            this._super.apply(this, arguments);
        },
    });
    
    view_registry.add('midashboard', miDashboardView);
    
    return miDashboardView;
});