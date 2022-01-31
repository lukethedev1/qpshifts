from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
import os
from QP_Shift.util import generar_excel
from QP_Shift.util import render_to_pdf
from django.conf import settings
from django.http import HttpResponse
from usuarios.models import Usuario
from QP_Shift.forms import InformacionPersonalForm
from shifts.filters import get_records
from shifts.forms import RecordFilterForm


@user_passes_test(lambda u: u.is_authenticated)
def home(request):
    template_name = 'records.html'

    filter_form = RecordFilterForm(request.GET or None)
    records, total_hours = get_records(filter_form)

    context = {
        'filter_form': filter_form,
        'records': records,
        'total_hours': total_hours
    }

    return render(request, template_name, context)


def logout_view(request):
    logout(request)

    return redirect('/login')


@user_passes_test(lambda u: u.is_authenticated)
def informacion_personal(request):
    form = InformacionPersonalForm(request.POST or None, instance=request.user.usuario, initial={'nombre': request.user.first_name, 'apellido': request.user.last_name, 'correo': request.user.email})

    if request.method == 'POST':

        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            nueva_clave = form.cleaned_data['nueva_clave']

            request.user.first_name = nombre
            request.user.last_name = apellido
            request.user.email = correo

            if nueva_clave:
                request.user.set_password(nueva_clave)

            request.user.save()
            form.save()

            messages.add_message(request, messages.SUCCESS, 'Información Personal actualizada exitosamente.')
            return redirect('inicio_admin')

    context = {
        'form': form,
        'usuario': request.user.usuario
    }

    return render(request, 'informacion-personal.html', context)


def cerrar_sesion(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Sesión cerrada exitosamente.')

    return redirect('login')
