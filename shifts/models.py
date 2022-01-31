from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    name = models.CharField('name', max_length=45)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        ordering = ['name']


class Location(models.Model):
    name = models.CharField('name', max_length=45)
    address = models.CharField('address', max_length=255)
    city = models.IntegerField('city', default=1, null=True)

    def __str__(self):
        return '%s, %s' % (self.name, self.address)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        ordering = ['name']


class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='locations', verbose_name='user')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, related_name='users', verbose_name='location')
    hour_value = models.IntegerField('city', default=12, null=True)

    def __str__(self):
        return '%s, %s' % (self.user, self.location)

    class Meta:
        verbose_name = 'userLocation'
        verbose_name_plural = 'userLocations'
        ordering = ['user']


class Record(models.Model):
    user_location = models.ForeignKey(UserLocation, on_delete=models.CASCADE, null=True, related_name='records', verbose_name='user_location')
    date_from = models.DateTimeField('date_from', auto_now_add=True)
    date_until = models.DateTimeField('date_until', blank=True, null=True)
    worked_hours = models.DurationField('worked_hours', blank=True, null=True)

    checkin_latitude = models.DecimalField('check in latitude', max_digits=15, decimal_places=9, blank=True, null=True)
    checkin_longitude = models.DecimalField('check in longitude', max_digits=15, decimal_places=9, blank=True, null=True)

    checkout_latitude = models.DecimalField('check out latitude', max_digits=15, decimal_places=9, blank=True, null=True)
    checkout_longitude = models.DecimalField('check out longitude', max_digits=15, decimal_places=9, blank=True, null=True)

    def __str__(self):
        return '%s, %s - %s' % (self.user_location.user, self.date_from, self.date_until)

    def calculate_worked_hours(self):
        timedelta = None

        if self.date_from and self.date_until:
            date_until = self.date_until.replace(tzinfo=None)
            date_from = self.date_from.replace(tzinfo=None)
            timedelta = date_until - date_from

        self.worked_hours = timedelta
        self.save()

    def get_worked_hours(self):
        days, seconds = self.worked_hours.days, self.worked_hours.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 60)
        return hours, minutes, seconds

    class Meta:
        verbose_name = 'record'
        verbose_name_plural = 'records'
        ordering = ['date_from']
