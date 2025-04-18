/** @mierp-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
const Widget = publicWidget.Widget;
import { renderToElement } from "@web/core/utils/render";
import { rpc } from "@web/core/network/rpc";

import miFieldIcon from "@mi_dashboard/js/component/general/mi_field_icon";

var miSelectDimension = Widget.extend({
    template: 'miSelectDimension',
    events: {
        'click .mi_select_dimension_item': '_onSelectDimension',
    },

    /**
     * @override
     */
    init: function (parent) {
        this._super.apply(this, arguments);

        this.parent = parent;
        this.fields = [];
    },

    willStart: function () {
        var self = this;

        return this._super.apply(this, arguments).then(function () {
            return self.load();
        });
    },

    load: function () {
        var self = this;
    },

    start: function () {
        var self = this;
        this._super.apply(this, arguments);
        // Add Content
        if (self.parent.selectedAnalysis) {
            rpc('/web/dataset/call_kw/mi.analysis/ui_get_analysis_info', {
                model: 'mi.analysis',
                method: 'ui_get_analysis_info',
                args: [self.parent.selectedAnalysis],
                kwargs: {},
            }).then(function (result) {
                // console.log('Get Dimensions', result)
                self.fields = result.fields_for_dimensions;
                self.fields.forEach(field => {
                    var $content = $(renderToElement('miSelectDimensionItem', {
                        name: field.name,
                        id: field.id,
                        field_type: field.field_type,
                        field_icon: miFieldIcon.getIcon(field.field_type),
                    }));
                    self.$el.append($content)
                });
            })
        }
    },

    /**
     * Private Method
     */
    _onSelectDimension: function (ev) {
        var self = this;
        var field_id = $(ev.currentTarget).data('id');
        if (self.parent.selectedAnalysis) {
            rpc('/web/dataset/call_kw/mi.analysis/ui_add_dimension_by_field', {
                model: 'mi.analysis',
                method: 'ui_add_dimension_by_field',
                args: [self.parent.selectedAnalysis, field_id],
                kwargs: {},
            }).then(function (result) {
                // console.log('Add Dimension', result);
                self.parent._loadAnalysisInfo();
                self.parent._onClickAddDimension();
                self.parent._renderVisual();
            })
        }
    },

    _getOwl: function () {
        var cur_obj = this;
        while (cur_obj) {
            if (cur_obj.__owl__) {
                return cur_obj;
            }
            cur_obj = cur_obj.parent;
        }
        return undefined;
    },
});

export default miSelectDimension;