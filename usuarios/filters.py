from django.db.models import Q
from .models import Usuario


def obtener_usuarios(request, filter_form):

    if filter_form.is_valid():

        q = filter_form.cleaned_data['q']

        search = q.split()

        if q and search:
            return Usuario.objects.filter(Q(user__first_name__icontains=q) | Q(user__last_name__icontains=q) | Q(user__first_name__in=search) | Q(user__last_name__in=search)).order_by('user__first_name')
        else:
            return Usuario.objects.order_by('user__first_name')
    else:

        return Usuario.objects.order_by('user__first_name')
