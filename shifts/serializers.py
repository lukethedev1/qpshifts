from rest_framework import serializers
import datetime
from django.utils import timezone
from rest_framework.fields import IntegerField

from shifts.models import UserLocation, Location, Record


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = UserLocation
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    user_location = UserLocationSerializer(read_only=True)
    user_location_id = IntegerField(write_only=True)

    def create(self, validated_data):
        user_location = validated_data.pop('user_location_id')
        checkin_latitude = validated_data.pop('checkin_latitude')
        checkin_longitude = validated_data.pop('checkin_longitude')

        return Record.objects.create(
            user_location=UserLocation.objects.get(id=user_location),
            checkin_latitude=float("{0:.9f}".format(checkin_latitude)),
            checkin_longitude=float("{0:.9f}".format(checkin_longitude))
        )

    def update(self, instance, validated_data):
        instance.date_until = datetime.datetime.now(tz=timezone.utc)
        instance.checkout_latitude = validated_data.pop('checkout_latitude')
        instance.checkout_longitude = validated_data.pop('checkout_longitude')
        instance.save()
        instance.calculate_worked_hours()

        return instance

    class Meta:
        model = Record
        fields = '__all__'
