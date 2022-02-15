jQuery(function () {
    jQuery('.datetimepicker').daterangepicker({
        timePicker: true,
        timePicker24Hour: true,
        showWeekNumbers: true,
        singleDatePicker: true,
        showDropdowns: true,
        minYear: 2020,
        locale: {
            format: "DD/MM/YYYY HH:mm",
            applyLabel: "Aceptar",
            cancelLabel: "Cancelar",
            weekLabel: '#',
            fromLabel: "Desde",
            toLabel: "Hasta",
            customRangeLabel: "Custom",
            daysOfWeek: [
                "Do",
                "Lu",
                "Ma",
                "Mi",
                "Ju",
                "Vi",
                "Sa"
            ],
            monthNames: [
                "Enero",
                "Febrero",
                "Marzo",
                "Abril",
                "Mayo",
                "Junio",
                "Julio",
                "Agosto",
                "Septiembre",
                "Octubre",
                "Noviembre",
                "Diciembre"
            ],
            firstDay: 1
        }
    });
});
