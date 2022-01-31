# coding=utf-8
from django import forms
from apps.menu.models import Perfil
from .models import Usuario


class UsuarioCreateForm(forms.ModelForm):

    usuario = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': u'Ingresa un usuario.'}
        )
    )

    clave = forms.CharField(
        required=False,
        label='Clave',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': u'Ingresa una nueva clave.'}
        )
    )

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': u'Ingresa un nombre.'}
        )
    )

    apellido = forms.CharField(
        label='Apellido',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': u'Ingresa un apellido.'}
        )
    )

    correo = forms.EmailField(
        required=False,
        label='Correo',
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': u'Ingresa un correo.'}
        )
    )

    perfil = forms.ModelChoiceField(
        queryset=Perfil.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control select-2'}
        )
    )

    class Meta:
        model = Usuario
        fields = ['usuario', 'clave', 'nombre', 'apellido', 'correo', 'perfil']


class UsuarioEditForm(forms.ModelForm):

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': u'Ingresa un nombre.'}
        )
    )

    apellido = forms.CharField(
        label='Apellido',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': u'Ingresa un apellido.'}
        )
    )

    correo = forms.EmailField(
        required=False,
        label='Correo',
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': u'Ingresa un correo.'}
        )
    )

    perfil = forms.ModelChoiceField(
        queryset=Perfil.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control select-2'}
        )
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'perfil']


class UsuarioFilterForm(forms.Form):

    q = forms.CharField(
        required=False,
        label='Buscar usuario',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': u'Buscar por nombreo o apellido.'}
        )
    )
