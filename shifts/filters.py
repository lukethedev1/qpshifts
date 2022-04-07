from shifts.models import Record


def get_records(filter_form):
    records = None

    if filter_form.is_valid():

        date_from = filter_form.cleaned_data.get('date_from')
        date_until = filter_form.cleaned_data.get('date_until')
        usuario = filter_form.cleaned_data.get('user')
        location = filter_form.cleaned_data.get('location')

        if date_from or date_until or usuario or location:
            records = Record.objects.all()

        if date_from:
            records = records.filter(date_from__gte=date_from)

        if date_until:
            records = records.filter(date_until__lte=date_until)

        if usuario:
            records = records.filter(user_location__user=usuario.user)

        if location:
            records = records.filter(user_location__location=location)

    if records is None:
        return records
    else:
        tempRecords = []

        for record in records.order_by('user_location__user').all():
            if len(tempRecords) == 0:
                record.tempVar = record.user_location.user.usuario.worked_hours(filter_form, record.user_location.user)
                tempRecords.append(record)
            else:
                if tempRecords[-1].user_location.user.pk != record.user_location.user.pk:
                    record.tempVar = record.user_location.user.usuario.worked_hours(filter_form, record.user_location.user)
                    tempRecords.append(record)

        return tempRecords


def get_records_detail(filter_form):
    records = None

    if filter_form.is_valid():

        date_from = filter_form.cleaned_data.get('date_from')
        date_until = filter_form.cleaned_data.get('date_until')
        usuario = filter_form.cleaned_data.get('user')
        location = filter_form.cleaned_data.get('location')

        if date_from or date_until or usuario or location:
            records = Record.objects.all()

        if date_from:
            records = records.filter(date_from__gte=date_from)

        if date_until:
            records = records.filter(date_until__lte=date_until)

        if usuario:
            records = records.filter(user_location__user=usuario.user)

        if location:
            records = records.filter(user_location__location=location)

    return records
