(function ($) {
    "use strict";

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
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {}
        });
    });
})(jQuery);
