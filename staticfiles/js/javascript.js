'use strict';

function validaRut(rut){

    let rutSolo = rut.substring(0, rut.length - 1);
    const verif = rut.charAt(rut.length - 1);

    let suma = 0;
    let continuar = true;

    for(let i = 2; continuar; i++) {
        suma += (rutSolo % 10) * i;
        rutSolo = parseInt(rutSolo) / 10;
        i = (i === 7) ? 1 : i;
        continuar = (rutSolo !== 0);
    }

    let resto = suma % 11;
    let dv = 11 - resto;

    if (dv === 10 && verif.toUpperCase() === 'K') return true;
    else if (dv === 11 && verif === 0) return true;
    else return dv === verif;
}

const formatNumber = {

    separador: ".",
    sepDecimal: ',',

    formatear: function (num) {
        num += '';
        let splitStr = num.split('.');
        let splitLeft = splitStr[0];
        let splitRight = splitStr.length > 1 ? this.sepDecimal + splitStr[1] : '';
        let regx = /(\d+)(\d{3})/;
        while (regx.test(splitLeft)) splitLeft = splitLeft.replace(regx, '$1' + this.separador + '$2');
        return this.simbol + splitLeft + splitRight;
    },
    new: function (num, simbol) {
        this.simbol = simbol || '';
        return this.formatear(num);
    }
};

function getDate(fecha){

    if (fecha) {
        let date = new Date(fecha);
        date.setMinutes(date.getMinutes() + date.getTimezoneOffset());
        return ("0" + date.getDate()).slice(-2) + "/" + ("0"+(date.getMonth()+1)).slice(-2) + "/" + date.getFullYear();
    }
}

function getTime(fecha){

    if (fecha) {
        let date = new Date(fecha);
        date.setMinutes(date.getMinutes() + date.getTimezoneOffset());
        return ("0" + date.getHours()).slice(-2) + ":" + ("0" + date.getMinutes()).slice(-2);
    }
}

function getDateTime(fecha){

    if (fecha) {
        let date = new Date(fecha);
        date.setMinutes(date.getMinutes() + date.getTimezoneOffset());
        return ("0" + date.getDate()).slice(-2) + "/" + ("0"+(date.getMonth()+1)).slice(-2) + "/" + date.getFullYear() + " " + ("0" + date.getHours()).slice(-2) + ":" + ("0" + date.getMinutes()).slice(-2);
    }
}

function getDateTimeTimeZone(fecha){

    if (fecha) {
        let date = new Date(fecha);
        return ("0" + date.getDate()).slice(-2) + "/" + ("0"+(date.getMonth()+1)).slice(-2) + "/" + date.getFullYear() + " " + ("0" + date.getHours()).slice(-2) + ":" + ("0" + date.getMinutes()).slice(-2);
    }
}

$(document).ready(function() {

    jQuery('.select-2').select2({
        language: "es",
        width: '100%'
    });

    $('[data-toggle="tooltip"]').tooltip();

    $('.test-popup-link').magnificPopup({
        gallery: {
            enabled: true
        },
        type: 'image'
    });

    $('th').click(function() {

        if (!$(this).hasClass("ordering-disabled")) {

            var table = $(this).parents('table').eq(0);
            var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()));
            this.asc = !this.asc;

            table.find('#ordering-icon').remove();

            if (!this.asc) {

                rows = rows.reverse();
                $(this).append('<span id="ordering-icon"> <i class="fas fa-sort-up"></i></span>');

            } else
                $(this).append('<span id="ordering-icon"> <i class="fas fa-sort-down"></i></span>');

            for (var i = 0; i < rows.length; i++) { table.append(rows[i]) }

        }
    });

    function comparer(index) {

        return function(a, b) {
            var valA = getCellValue(a, index), valB = getCellValue(b, index);
            return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.toString().localeCompare(valB)
        }
    }

    function getCellValue(row, index) {

        try {

            if ($(row).children('td').eq(index).data('ordering')) { return $(row).children('td').eq(index).data('ordering'); }
            else return $(row).children('td').eq(index).text();

        } catch (error) { console.log(error);}
    }

    function fontAwesomeTemplate(icon) {

        if (!icon.id) { return icon.text; }
		return $('<div><i class="' + icon.element.value + '"></i> ' +  icon.text + '</div>');
	};

    $(".icon-select").select2({
		templateResult: fontAwesomeTemplate,
		templateSelection: fontAwesomeTemplate
	});

    setTimeout(function(){$("#mensaje").fadeOut(500);},5000);

    $('#confirm-delete').on('show.bs.modal',function(e){
        $('#eliminar-permanente').data('id',$(e.relatedTarget).data('id'));
        $('#eliminar-permanente').data('url',$(e.relatedTarget).data('url'));
        $('#eliminar-permanente').data('nombre',$(e.relatedTarget).data('nombre'));
        $('#eliminar-permanente').data('html',$(e.relatedTarget).data('html'));
        $('#confirm-delete-header').text($(e.relatedTarget).data('title'));
        $('#confirm-delete-body').html($(e.relatedTarget).data('content'));
    });

    $('#eliminar-permanente').click(function(){

        jQuery('#cargando').modal('show');

        var id = $(this).data('id');
        var url = $(this).data('url');
        var nombre = $(this).data('nombre');
        var html = $(this).data('html');

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'id' : id,
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data){

                jQuery('#cargando').modal('hide');

                if(html){
                    jQuery('#confirm-delete').modal('hide');
                    var mensaje = '<div class="alert alert-success alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><span class="glyphicon glyphicon-ok-circle"></span> '+nombre+' eliminado exitosamente.</div>';
                    $('#mensaje').html(mensaje).show();
                    $(html).remove();
                }else
                    location.reload();
            }
        });
    });

    $('.datepicker').datetimepicker({
        locale: 'es',
        ignoreReadonly: true,
        format: 'DD/MM/YYYY',
        showClose: true,
        showClear:true
    });

    $('.timepicker').datetimepicker({
        locale: 'es',
        ignoreReadonly: true,
        format: 'HH:mm',
        showClose: true,
        stepping: 5,
        useCurrent: false,
        showClear:true
    });

    $('.timepicker-1').datetimepicker({
        locale: 'es',
        ignoreReadonly: true,
        format: 'HH:mm',
        showClose: true,
        stepping: 1,
        useCurrent: false,
        showClear:true
    });

    $('.datetimepicker').datetimepicker({
        locale: 'es',
        ignoreReadonly: true,
        format: 'DD/MM/YYYY HH:mm',
        showClose: true,
        stepping: 5,
        sideBySide:true,
        useCurrent: false,
        showClear:true,
        toolbarPlacement: "top",
    });

    $('.datetimepicker-1').datetimepicker({
        locale: 'es',
        ignoreReadonly: true,
        format: 'DD/MM/YYYY HH:mm',
        showClose: true,
        stepping: 1,
        sideBySide:true,
        useCurrent: false,
        showClear:true
    });

    $('#id_fecha_salida_grupo').datetimepicker();
    $('#id_fecha_llegada_grupo').datetimepicker();

    $("#id_fecha_salida_grupo").on("dp.change", function (e){
        $('#fecha-salida-viaje').text(e.date.format("DD/MM/YYYY"));
        $('#hora-salida-viaje').text(e.date.format("HH:mm")+' hrs.');
        $('#id_fecha_llegada_grupo').data("DateTimePicker").minDate(e.date);
    });

    $("#id_fecha_llegada_grupo").on("dp.change", function (e){
        $('#fecha-llegada-viaje').text(e.date.format("DD/MM/YYYY"));
        $('#hora-llegada-viaje').text(e.date.format("HH:mm")+' hrs.');
        $('#id_fecha_salida_grupo').data("DateTimePicker").maxDate(e.date);
    });
});
