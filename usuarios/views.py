from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .filters import obtener_usuarios
from .forms import UsuarioCreateForm, UsuarioFilterForm, UsuarioEditForm
from .models import Usuario
from .util import has_perm
import json


@user_passes_test(lambda u: has_perm(u, 'view_usuario'))
def usuarios(request):

    template_name = 'usuarios.html'

    filter_form = UsuarioFilterForm(request.GET or None)
    usuarios = obtener_usuarios(request, filter_form)

    context = {
        'usuarios': usuarios,
        'filter_form': filter_form,
    }

    return render(request, template_name, context)


@user_passes_test(lambda u: has_perm(u, 'add_usuario'))
def agregar_usuario(request):

    form = UsuarioCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':

        if form.is_valid():

            try:

                user = User.objects.create_user(username=request.POST['usuario'], email=request.POST['correo'], password=request.POST['clave'], first_name=request.POST['nombre'], last_name=request.POST['apellido'])

                usuario = form.save()
                usuario.user = user
                usuario.save()

                messages.add_message(request, messages.SUCCESS, 'Usuario agregado exitosamente.')
                return redirect('/editar-usuario/' + str(usuario.pk) + '?menu=personal')

            except IntegrityError:
                messages.add_message(request, messages.ERROR, 'El usuario ya existe.')

    template_name = 'agregar-usuario.html'

    context = {
        'form': form
    }

    return render(request, template_name, context)


@user_passes_test(lambda u: has_perm(u, 'change_usuario'))
def editar_usuario(request, id):

    usuario = get_object_or_404(Usuario, id=id)

    form = UsuarioEditForm(request.POST or None, instance=usuario, initial={'nombre': usuario.user.first_name, 'apellido': usuario.user.last_name, 'correo': usuario.user.email})

    if request.method == 'POST':

        if form.is_valid():

            usuario.user.first_name = request.POST['nombre']
            usuario.user.last_name = request.POST['apellido']
            usuario.user.email = request.POST['correo']
            usuario.user.save()

            usuario = form.save()

            messages.add_message(request, messages.SUCCESS, 'Usuario actualizado exitosamente.')

            return redirect('usuarios')

    template_name = 'editar-usuario.html'

    context = {
        'usuario': usuario,
        'form': form,
        'menu': request.GET.get('menu')
    }

    return render(request, template_name, context)


@user_passes_test(lambda u: has_perm(u, 'delete_usuario'))
def ajax_eliminar_usuario(request):

    if request.method == 'POST':

        usuario = Usuario.objects.get(pk=request.POST['id'])
        usuario.user.delete()
        usuario.delete()
        messages.add_message(request, messages.SUCCESS, 'Usuario eliminado exitosamente.')
        return HttpResponse('')
    else:
        return redirect('/')
