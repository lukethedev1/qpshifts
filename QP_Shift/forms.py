from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from django import forms

from usuarios.models import Usuario


class InformacionPersonalForm(forms.ModelForm):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()

    clave_actual = forms.CharField(required=False)
    nueva_clave = forms.CharField(required=False)
    confirmar_nueva_clave = forms.CharField(required=False)

    class Meta:
        model = Usuario
        exclude = ['user', 'tipo', 'telefono_adicional', 'rut', 'fecha_creacion', 'comercio', 'perfil', 'habilitado', 'collapse_menu', 'comunas']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'form'

        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6 mb-0'),
                Column('apellido', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('correo', css_class='form-group col-md-6 mb-0'),
                Column('telefono', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML('<h1 class="mt-5">Cambiar Clave</h1>'),
            HTML('<p class="small"><i class="far fa-lightbulb"></i> Si quieres actualizar tu clave, ingrésala en los campos correspondientes, de lo contrario, deja los campos vacíos.</p>'),
            'clave_actual',
            Row(
                Column('nueva_clave', css_class='form-group col-md-6 mb-0'),
                Column('confirmar_nueva_clave', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            )
        )

    def clean(self):

        cleaned_data = super().clean()

        clave_actual = cleaned_data.get('clave_actual')
        nueva_clave = cleaned_data.get('nueva_clave')
        confirmar_nueva_clave = cleaned_data.get('confirmar_nueva_clave')

        if nueva_clave and not confirmar_nueva_clave:
            raise forms.ValidationError('Debes confirmar la nueva clave.')

        elif confirmar_nueva_clave and not nueva_clave:
            raise forms.ValidationError('Debes ingresar la nueva clave.')

        elif nueva_clave and confirmar_nueva_clave and nueva_clave != confirmar_nueva_clave:
            raise forms.ValidationError('Las claves no coinciden.')

        elif nueva_clave and confirmar_nueva_clave and not self.instance.user.check_password(clave_actual):
            raise forms.ValidationError('Tu clave actual no es correcta.')
