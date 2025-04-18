mierp.define('mi_dashboard.miDashboardModel', function (require) {
    "use strict";

    var AbstractModel = require('web.AbstractModel');
    return AbstractModel.extend({
        init: function () {
            this._super.apply(this, arguments);
        },
    });

});