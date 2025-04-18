mierp.define('mi_dashboard.miAnalysisController', function (require) {
    "use strict";

    var AbstractController = require('web.AbstractController');
    return AbstractController.extend({
        init: function (parent, model, renderer, params) {
            params.viewType = "mianalysis";
            this._super.apply(this, arguments);
        }
    });

});