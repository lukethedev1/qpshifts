from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets, mixins
from django.contrib.auth import authenticate
from shifts.models import UserLocation, Record
from shifts.serializers import UserLocationSerializer, RecordSerializer
from usuarios.serializer import UserSerializer


class AuthViewSet(viewsets.ViewSet):
    queryset = User.objects.none()
    serializer_class = UserSerializer

    def list(self, request):

        username = self.request.query_params.get('username', False)
        password = self.request.query_params.get('password', False)

        user = authenticate(username=username, password=password)

        if user is not None:
            return JsonResponse(user.id, safe=False)
        else:
            return JsonResponse(0, safe=False)


class LocationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserLocation.objects.none()
    serializer_class = UserLocationSerializer


class UserLocationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer

    def get_queryset(self):
        return UserLocation.objects.filter(user__pk=self.kwargs['user_pk'])


class RecordsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Record.objects.none()
    serializer_class = RecordSerializer

    def perform_create(self, serializer):
        serializer.save()


class LastRecordViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Record.objects.none()
    serializer_class = RecordSerializer

    def retrieve(self, request, **kwargs):

        user_records = Record.objects.filter(user_location__user=self.request.user)

        if user_records and user_records.filter(date_until__isnull=True).last():
            return JsonResponse(RecordSerializer(user_records.filter(date_until__isnull=True).last()).data, safe=False)
        else:
            return JsonResponse({}, safe=False)

    def update(self, request, *args, **kwargs):

        user_records = Record.objects.filter(user_location__user=self.request.user)
        last_record = user_records.filter(date_until__isnull=True).last()

        serializer = RecordSerializer(last_record, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, safe=False)