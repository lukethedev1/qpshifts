jQuery(function () {

    'use strict';

    const datetimePicker = jQuery('.datetimepicker');

    datetimePicker.daterangepicker({
        timePicker: true,
        timePicker24Hour: true,
        showWeekNumbers: true,
        singleDatePicker: true,
        showDropdowns: true,
        minYear: 2020,
        autoUpdateInput: false,
        locale: {
            format: 'DD/MM/YYYY HH:mm',
            applyLabel: 'Aceptar',
            cancelLabel: 'Limpiar',
            weekLabel: '#',
            fromLabel: 'Desde',
            toLabel: 'Hasta',
            customRangeLabel: 'Custom',
            daysOfWeek: [
                'Do',
                'Lu',
                'Ma',
                'Mi',
                'Ju',
                'Vi',
                'Sa'
            ],
            monthNames: [
                'Enero',
                'Febrero',
                'Marzo',
                'Abril',
                'Mayo',
                'Junio',
                'Julio',
                'Agosto',
                'Septiembre',
                'Octubre',
                'Noviembre',
                'Diciembre'
            ],
            firstDay: 1
        }
    });

    datetimePicker.on('apply.daterangepicker', function(ev, picker) {
        jQuery(this).val(picker.startDate.format('DD/MM/YYYY HH:mm'));
    });

    datetimePicker.on('cancel.daterangepicker', function(_, __) {
        jQuery(this).val('');
    });
});
