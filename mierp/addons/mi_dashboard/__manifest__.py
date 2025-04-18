# -*- coding: utf-8 -*-
{
    "name": """MiERP Dashboard with AI""",
    "summary": """
        Beautiful Analytic Dashboard by MiERP.
        You can create a Sales Dashboard, Inventory Dashboard, Finance Dashboard, or Others dynamically with this module.
        You can explore data with AI too!
    """,
    "category": "My Apps MiERP/Mi_Dashboard",
    "version": "18.0.5.2.1",
    "development_status": "Production",  # Options: Alpha|Beta|Production/Stable|Mature
    "auto_install": False,
    "installable": True,
    "application": True,
    "author": "MiERP",
    "license": "LGPL-3",
    "images": [
        'static/description/banner.gif'
    ],
    "depends": [
        # mierp addons
        'base',
        'web',
        # third party addons

        # developed addons
        'mi_data',
    ],
    "data": [
        # group
        'security/res_groups.xml',

        # data
        'data/mi_visual_type.xml',
        'data/mi_visual_config.xml',
        'data/mi_visual_config_value.xml',
        'data/mi_dashboard_theme.xml',
        'data/mi_data_template.xml',

        # global action
        # 'views/action/action.xml',

        # view
        'views/common/mi_dashboard.xml',
        'views/common/mi_analysis.xml',
        'views/common/mi_lab_api_key_wizard.xml',
        'views/common/res_company.xml',

        # wizard
        'views/wizard/mi_dashboard_config_wizard.xml',

        # report paperformat
        # 'data/report_paperformat.xml',

        # report template
        # 'views/report/report_template_model_name.xml',

        # report action
        # 'views/action/action_report.xml',

        # assets
        # 'views/assets.xml',

        # onboarding action
        # 'views/action/action_onboarding.xml',

        # action menu
        'views/action/action_menu.xml',

        # action onboarding
        # 'views/action/action_onboarding.xml',

        # menu
        'views/menu.xml',

        # security
        'security/ir.model.access.csv',
        # 'security/ir.rule.csv',

        # template
        'views/template/mi_dashboard.xml',
        'views/template/mi_dashboard_slide.xml',
    ],
    "demo": [
        # 'demo/demo.xml',
    ],
    "qweb": [

    ],

    "post_load": None,
    # "pre_init_hook": "pre_init_hook",
    # "post_init_hook": "post_init_hook",
    "uninstall_hook": None,

    "external_dependencies": {"python": [], "bin": []},
    "live_test_url": "https://demo.miapp.id/web/login",
    # "demo_title": "{MODULE_NAME}",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    "demo_url": "https://demo.miapp.id/web/login",
    # "demo_summary": "{SHORT_DESCRIPTION_OF_THE_MODULE}",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]

    'assets': {
        'web.assets_backend': [
            # mierp
            'web/static/src/legacy/js/core/class.js',
            'web/static/src/core/dialog/dialog.js',
            'web/static/src/core/dialog/dialog.xml',
            'web/static/src/legacy/js/public/minimal_dom.js',
            # 'web/static/src/legacy/js/core/dom.js',
            # 'web/static/src/legacy/js/core/mixins.js',
            # 'web/static/src/legacy/js/core/service_mixins.js',
            'web/static/src/legacy/js/public/public_widget.js',
            'web/static/lib/jquery/jquery.js',
            # QWeb
            # Generic
            'mi_dashboard/static/src/xml/component/mi_dialog.xml',
            # Component
            'mi_dashboard/static/src/xml/component/mi_view_dashboard.xml',
            'mi_dashboard/static/src/xml/component/mi_view_dashboard_block.xml',
            'mi_dashboard/static/src/xml/component/mi_view_analysis.xml',
            'mi_dashboard/static/src/xml/component/mi_config_analysis.xml',
            'mi_dashboard/static/src/xml/component/mi_view_table.xml',
            'mi_dashboard/static/src/xml/component/mi_view_visual.xml',
            'mi_dashboard/static/src/xml/component/mi_config_dashboard.xml',
            'mi_dashboard/static/src/xml/component/mi_select_analysis.xml',
            'mi_dashboard/static/src/xml/component/mi_select_dashboard.xml',
            'mi_dashboard/static/src/xml/component/mi_select_metric.xml',
            'mi_dashboard/static/src/xml/component/mi_select_dimension.xml',
            'mi_dashboard/static/src/xml/component/mi_select_sort.xml',
            'mi_dashboard/static/src/xml/component/mi_select_filter_temp.xml',
            'mi_dashboard/static/src/xml/component/mi_select_filter.xml',
            # Component > QWeb
            'mi_dashboard/static/src/xml/component/qweb/mi_select_analysis_item.xml',
            'mi_dashboard/static/src/xml/component/qweb/mi_select_dashboard_item.xml',
            'mi_dashboard/static/src/xml/component/qweb/mi_select_metric_item.xml',
            'mi_dashboard/static/src/xml/component/qweb/mi_select_dimension_item.xml',
            'mi_dashboard/static/src/xml/component/qweb/mi_select_filter_item.xml',
            'mi_dashboard/static/src/xml/component/qweb/mi_select_sort_item.xml',
            # Base
            'mi_dashboard/static/src/xml/mi_dashboard.xml',
            'mi_dashboard/static/src/xml/mi_analysis.xml',
            'mi_dashboard/static/src/xml/mi_analysis_widget.xml',

            # CSS
            'mi_dashboard/static/lib/select2/select2.css',
            'mi_dashboard/static/lib/select2-bootstrap-css/select2-bootstrap.css',
            'mi_dashboard/static/lib/gridstack/gridstack.min.css',
            'mi_dashboard/static/lib/grid/mermaid.min.css',
            'mi_dashboard/static/lib/google/icon.css',
            'mi_dashboard/static/lib/jquery.ui/jquery-ui.css',
            'mi_dashboard/static/lib/bootstrap-datepicker/css/bootstrap-datepicker3.min.css',
            'mi_dashboard/static/lib/bootstrap-datepicker/css/bootstrap-datepicker.min.css',
            'mi_dashboard/static/lib/tempusdominus/tempusdominus.min.css',
            'mi_dashboard/static/lib/google/icon.css',

            'mi_dashboard/static/src/css/font.css',
            'mi_dashboard/static/src/css/component/general/mi_bootstrap.min.css',
            'mi_dashboard/static/src/css/component/general/mi_layout.css',
            'mi_dashboard/static/src/css/component/general/mi_dialog.css',
            'mi_dashboard/static/src/css/component/general/mi_button.css',
            'mi_dashboard/static/src/css/component/general/mi_select.css',
            'mi_dashboard/static/src/css/component/general/mi_accordion.css',
            'mi_dashboard/static/src/css/component/general/mi_chart.css',
            'mi_dashboard/static/src/css/component/general/mi_replace.css',

            'mi_dashboard/static/src/css/component/main/mi_view.css',
            'mi_dashboard/static/src/css/component/main/mi_view_table.css',
            'mi_dashboard/static/src/css/component/main/mi_view_dashboard.css',
            'mi_dashboard/static/src/css/component/main/mi_config_analysis.css',
            'mi_dashboard/static/src/css/component/main/mi_config_dashboard.css',
            'mi_dashboard/static/src/css/component/main/mi_select_analysis.css',
            'mi_dashboard/static/src/css/component/main/mi_select_metric.css',
            'mi_dashboard/static/src/css/component/main/mi_select_dimension.css',
            'mi_dashboard/static/src/css/component/main/mi_select_sort.css',
            'mi_dashboard/static/src/css/component/main/mi_select_filter_temp.css',
            'mi_dashboard/static/src/css/component/main/mi_select_filter.css',
            'mi_dashboard/static/src/css/component/main/mi_description_page.css',

            'mi_dashboard/static/src/css/component/toggle-switchy.css',

            # JS
            'mi_dashboard/static/lib/jquery.ui/jquery-ui.js',
            'mi_dashboard/static/lib/select2/select2.js',
            'mi_dashboard/static/lib/moment/moment.js',
            'mi_dashboard/static/lib/ace-1.3.1/ace.js',
            'mi_dashboard/static/lib/ace-1.3.1/mode-javascript.js',
            'mi_dashboard/static/lib/ace-1.3.1/worker-javascript.js',
            'mi_dashboard/static/lib/ace-1.3.1/theme-chrome.js',
            'mi_dashboard/static/lib/ace-1.3.1/mode-sql.js',
            'mi_dashboard/static/lib/ace-1.3.1/theme-chrome.js',
            'mi_dashboard/static/lib/amcharts/core.js',
            'mi_dashboard/static/lib/amcharts/charts.js',
            'mi_dashboard/static/lib/amcharts/maps.js',
            'mi_dashboard/static/lib/amcharts/regression.js',
            'mi_dashboard/static/lib/amcharts/geodata/indonesiaLow.js',
            'mi_dashboard/static/lib/amcharts/geodata/usaLow.js',
            'mi_dashboard/static/lib/amcharts/geodata/worldLow.js',
            'mi_dashboard/static/lib/amcharts/geodata/countries2.js',
            'mi_dashboard/static/lib/amcharts/themes/animated.js',
            'mi_dashboard/static/lib/amcharts/themes/frozen.js',
            'mi_dashboard/static/lib/gridstack/gridstack-h5.js',
            # 'mi_dashboard/static/lib/gridstack/gridstack-poly.js',
            # 'mi_dashboard/static/lib/gridstack/gridstack-all.js',
            'mi_dashboard/static/lib/sweetalert/sweetalert.min.js',
            'mi_dashboard/static/lib/xlsx/xlsx.full.min.js',
            'mi_dashboard/static/lib/grid/gridjs.umd.js',
            'mi_dashboard/static/lib/jspdf/html2canvas.min.js',
            'mi_dashboard/static/lib/jspdf/jspdf.umd.min.js',
            'mi_dashboard/static/lib/jquery.ui/jquery-ui.js',
            'mi_dashboard/static/lib/bootstrap-datepicker/js/bootstrap-datepicker.min.js',
            'mi_dashboard/static/lib/bootstrap-datepicker/js/bootstrap-datepicker-conflict.js',
            'mi_dashboard/static/lib/jscolor/jscolor.min.js',

            'mi_dashboard/static/lib/tempusdominus/tempusdominus.min.js',
            'mi_dashboard/static/src/js/component/chart/amcharts_theme.js',
            'mi_dashboard/static/src/js/component/chart/amcharts_component_old.js',
            'mi_dashboard/static/src/js/component/chart/amcharts_component.js',
            'mi_dashboard/static/src/js/component/general/mi_autocomplete.js',
            'mi_dashboard/static/src/js/component/general/mi_tags.js',
            'mi_dashboard/static/src/js/component/general/mi_dialog.js',
            'mi_dashboard/static/src/js/component/general/mi_field_icon.js',
            'mi_dashboard/static/src/js/component/general/mi_dropdown.js',
            'mi_dashboard/static/src/js/component/main/mi_view_dashboard.js',
            'mi_dashboard/static/src/js/component/main/mi_view_dashboard_block.js',
            'mi_dashboard/static/src/js/component/main/mi_view_analysis.js',
            'mi_dashboard/static/src/js/component/main/mi_view_table.js',
            'mi_dashboard/static/src/js/component/main/mi_view_visual.js',
            'mi_dashboard/static/src/js/component/main/mi_config_dashboard.js',
            'mi_dashboard/static/src/js/component/main/mi_config_analysis.js',
            'mi_dashboard/static/src/js/component/main/mi_select_analysis.js',
            'mi_dashboard/static/src/js/component/main/mi_select_dashboard.js',
            'mi_dashboard/static/src/js/component/main/mi_select_metric.js',
            'mi_dashboard/static/src/js/component/main/mi_select_dimension.js',
            'mi_dashboard/static/src/js/component/main/mi_select_sort.js',
            'mi_dashboard/static/src/js/component/main/mi_select_filter_temp.js',
            'mi_dashboard/static/src/js/component/main/mi_select_filter.js',
            'mi_dashboard/static/src/js/component/main/mi_add_analysis.js',
            'mi_dashboard/static/src/js/mi_analysis_controller.js',
            'mi_dashboard/static/src/js/mi_analysis_view.js',
            'mi_dashboard/static/src/js/mi_dashboard_controller.js',
            'mi_dashboard/static/src/js/mi_dashboard_view.js',
            'mi_dashboard/static/src/js/mi_analysis_widget.js',
            'mi_dashboard/static/src/js/mi_slide.js',
        ]
    }
}
