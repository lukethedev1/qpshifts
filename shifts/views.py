from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from shifts.filters import get_records, get_records_detail
from shifts.forms import RecordFilterForm
from shifts.models import Record
from django.shortcuts import render, redirect, get_object_or_404
import os
from QP_Shift.util import generar_excel, generar_excel_detalle
from QP_Shift.util import render_to_pdf
from django.conf import settings
from django.http import HttpResponse


@user_passes_test(lambda u: u.is_authenticated)
def records(request):
    template_name = 'records.html'

    filter_form = RecordFilterForm(request.GET or None)
    records = get_records(filter_form)

    context = {
        'filter_form': filter_form,
        'records': records
    }

    return render(request, template_name, context)


@user_passes_test(lambda u: u.is_authenticated)
def cerrar_registro(request):
    pk = request.POST.get('pk', None)

    if pk:

        record = Record.objects.filter(pk=pk).first()

        if record:
            record.date_until = timezone.now()
            record.save()

            messages.add_message(request, messages.SUCCESS, 'Record updated successfully.')

    return redirect('records')


@user_passes_test(lambda u: u.is_authenticated)
def records_detail(request):
    template_name = 'records-detail.html'

    filter_form = RecordFilterForm(request.GET or None)
    records = get_records_detail(filter_form)

    context = {
        'filter_form': filter_form,
        'records': records
    }

    return render(request, template_name, context)


@user_passes_test(lambda u: u.is_authenticated)
def exportar_registros_excel(request):
    filter_form = RecordFilterForm(request.GET or None)
    records = get_records(filter_form)

    excel = generar_excel(records, filter_form)
    return excel


@user_passes_test(lambda u: u.is_authenticated)
def exportar_detalle_registros_excel(request):
    filter_form = RecordFilterForm(request.GET or None)
    records = get_records_detail(filter_form)

    excel = generar_excel_detalle(records)
    return excel


@user_passes_test(lambda u: u.is_authenticated)
def exportar_registros_pdf(request):
    filter_form = RecordFilterForm(request.GET or None)
    records = get_records(filter_form)

    context = {
        'filter_form': filter_form,
        'registros': records,
        'url_logo': os.path.join(settings.STATICFILES_DIRS[0], 'images/trazasur-logo.png'),
    }

    pdf = render_to_pdf('pdf/registros.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


@user_passes_test(lambda u: u.is_authenticated)
def exportar_detalle_registros_pdf(request):
    filter_form = RecordFilterForm(request.GET or None)
    records = get_records_detail(filter_form)

    context = {
        'filter_form': filter_form,
        'registros': records,
        'url_logo': os.path.join(settings.STATICFILES_DIRS[0], 'images/trazasur-logo.png'),
    }

    pdf = render_to_pdf('pdf/detalle-registros.html', context)
    return HttpResponse(pdf, content_type='application/pdf')