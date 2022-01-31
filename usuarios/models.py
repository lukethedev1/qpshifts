from django.contrib.auth.models import User
from django.db import models
from shifts.filters import get_records_detail


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='usuario', verbose_name='usuario')

    telefono = models.CharField('teléfono', max_length=10, null=True, blank=True)

    HABILITADO = 'HABILITADO'
    NO_HABILITADO = 'NO_HABILITADO'

    ESTADOS = (
        (HABILITADO, 'Habilitado'),
        (NO_HABILITADO, 'No Habilitado')
    )

    estado = models.CharField(
        'estado',
        max_length=13,
        choices=ESTADOS,
        default=HABILITADO,
        blank=True
    )

    def worked_hours(self, filter_form, user):

        records = get_records_detail(filter_form)
        filtered_records = records.all().filter(user_location__user=user, worked_hours__isnull=False)

        value = None
        for record in filtered_records:
            if record == filtered_records.first():
                value = record.worked_hours
            else:
                value += record.worked_hours

        return value

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['user__first_name']

    def __str__(self):

        if self.user:

            full_name = self.user.get_full_name()

            if full_name:
                return '%s' % full_name
            else:
                return self.user.username

        return ''
