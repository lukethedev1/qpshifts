(function ($) {
    "use strict";

    const eliminar = $('#eliminar-permanente');
    const cargando = jQuery('#cargando');
    const confirmarEliminacion = $('#confirm-delete');

    confirmarEliminacion.on('show.bs.modal', function (e) {

        eliminar.data('id', $(e.relatedTarget).data('id'));
        eliminar.data('url', $(e.relatedTarget).data('url'));
        eliminar.data('nombre', $(e.relatedTarget).data('nombre'));
        eliminar.data('html', $(e.relatedTarget).data('html'));
        $('#confirm-delete-header').text($(e.relatedTarget).data('title'));
        $('#confirm-delete-body').html($(e.relatedTarget).data('content'));
    });

    eliminar.click(function () {

        cargando.modal('show');

        const id = $(this).data('id');
        const url = $(this).data('url');

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'id': id,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {

                cargando.modal('hide');

                if (!data) {

                    confirmarEliminacion.modal('hide');
                    const mensaje = `<div class="alert alert-danger alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><i class="fas fa-times"></i> Error al intentar eliminar el elemento.</div>`;
                    $('#mensaje').html(mensaje).show();

                } else {
                    location.reload();
                }
            }
        });
    });

    const path = window.location.href;

    $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function () {
        if (this.href === path) {
            $(this).addClass('active');
        }
    });

    let activatedPath = window.location.pathname;

    if (!activatedPath) {
        activatedPath = '/';
    }

    let targetAnchor = $('[href="' + activatedPath + '"]');
    let collapseAncestors = targetAnchor.parents('.collapse');

    collapseAncestors.each(function () {
        console.log(1);
        $(this).addClass('show');
        $('[data-target="#' + this.id + '"]').removeClass('collapsed');

    });

    $('#sidebarToggle').click(function (e) {

        e.preventDefault();
        $('body').toggleClass('sb-sidenav-toggled');

        $.ajax({
            type: 'POST',
            url: '/admin/actualizar-estado-menu/',
            data: {
                'estado': $("body").hasClass("sb-sidenav-toggled"),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
            }
        });
    });
})(jQuery);
