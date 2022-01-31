from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django import forms

from shifts.models import Location
from usuarios.models import Usuario
from QP_Shift.util import DateTimeInput


class RecordFilterForm(forms.Form):

    date_from = forms.DateTimeField(
        input_formats=[
            "%d/%m/%Y %H:%M:%S",
            "%d/%m/%Y %H:%M:%S.%f",
            "%d/%m/%Y %H:%M",
            "%d/%m/%y %H:%M:%S",
            "%d/%m/%y %H:%M:%S.%f",
            "%d/%m/%y %H:%M",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M:%S.%f",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d"
        ],
        required=False,
        label='From',
        widget=DateTimeInput()
    )

    date_until = forms.DateTimeField(
        input_formats=[
            "%d/%m/%Y %H:%M:%S",
            "%d/%m/%Y %H:%M:%S.%f",
            "%d/%m/%Y %H:%M",
            "%d/%m/%y %H:%M:%S",
            "%d/%m/%y %H:%M:%S.%f",
            "%d/%m/%y %H:%M",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M:%S.%f",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d"
        ],
        required=False,
        label='Until',
        widget=DateTimeInput()
    )

    location = forms.ModelChoiceField(
        required=False,
        label='Location',
        queryset=Location.objects.all()
    )

    user = forms.ModelChoiceField(
        required=False,
        label='User',
        queryset=Usuario.objects.all()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'form'
        self.helper.form_method = 'get'
        self.fields['user'].widget.attrs = {'class': 'form-control select-2'}

        self.helper.layout = Layout(
            Row(
                Column('date_from', css_class='form-group col-md-3 mb-0'),
                Column('date_until', css_class='form-group col-md-3 mb-0'),
                Column('location', css_class='form-group col-md-3 mb-0'),
                Column('user', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            )
        )

    def clean(self):

        cleaned_data = super().clean()

        date_from = cleaned_data.get('date_from')
        date_until = cleaned_data.get('date_until')

        if date_from and date_until and date_until < date_from:
            raise forms.ValidationError('Until date can not be higher than From date.')