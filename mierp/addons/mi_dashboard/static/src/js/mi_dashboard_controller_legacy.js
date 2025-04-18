mierp.define('mi_dashboard.miDashboardController', function (require) {
    "use strict";

    var AbstractController = require('web.AbstractController');
    return AbstractController.extend({
        init: function (parent, model, renderer, params) {
            params.viewType = "midashboard";
            this._super.apply(this, arguments);
        }
    });

});