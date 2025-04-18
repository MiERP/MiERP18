// Dropdown, Datepicker and Collapse are not working in mierp Version 16
// So this is the manual event listener
$(function () {
    $('body').on('click', '.mi_view', function (ev) {
        ev.stopPropagation();
        let elmId = $(ev.currentTarget);

        $('.dropdown-menu').hide();
    });

    $('body').on('click', '.mi_view .dropdown-toggle', function (ev) {
        ev.stopPropagation();
        let elmId = $(ev.currentTarget);

        if (($(elmId).parents().find('.mi_view').length) >= 1) {
            if ($(elmId).hasClass('show') || $(elmId).parent().find('.dropdown-menu').css('display') == 'none') {
                $(elmId).removeClass('.dropdown-menu');
                $('.dropdown-menu').hide();
                $(elmId).addClass('.dropdown-menu');
                $(elmId).removeClass('show');
                $(elmId).parent().find('.dropdown-menu').show();
            } else {
                $(elmId).removeClass('.dropdown-menu');
                $('.dropdown-menu').hide();
                $(elmId).addClass('.dropdown-menu');
                $(elmId).addClass('show');
                $(elmId).parent().find('.dropdown-menu').hide();
            }
        }


    });

    $('body').on('click', '.mi_view .o_datepicker', function (ev) {
        ev.stopPropagation();
        let elmId = $(ev.currentTarget);

        if (($(elmId).parents().find('.mi_view').length) >= 1) {
            $('.bootstrap-datetime-picker').show();
        }
    });
    $('body').on('click', '.mi_view [data-toggle="collapse"]', function (ev) {
        ev.stopPropagation();
        let elmId = $(ev.currentTarget).data('target');

        if (($(elmId).parents().find('.mi_view').length) >= 1) {
            if ($(elmId).hasClass('show')) {
                $(elmId).removeClass('show');
            } else {
                $(elmId).addClass('show');
            }
        };
    });
});