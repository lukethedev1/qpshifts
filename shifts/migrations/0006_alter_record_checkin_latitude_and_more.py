# Generated by Django 4.0 on 2022-01-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0005_remove_record_user_userlocation_hour_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='checkin_latitude',
            field=models.DecimalField(blank=True, decimal_places=9, max_digits=50, null=True, verbose_name='check in latitude'),
        ),
        migrations.AlterField(
            model_name='record',
            name='checkin_longitude',
            field=models.DecimalField(blank=True, decimal_places=9, max_digits=50, null=True, verbose_name='check in longitude'),
        ),
        migrations.AlterField(
            model_name='record',
            name='checkout_latitude',
            field=models.DecimalField(blank=True, decimal_places=9, max_digits=50, null=True, verbose_name='check out latitude'),
        ),
        migrations.AlterField(
            model_name='record',
            name='checkout_longitude',
            field=models.DecimalField(blank=True, decimal_places=9, max_digits=50, null=True, verbose_name='check out longitude'),
        ),
    ]
