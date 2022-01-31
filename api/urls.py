from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter
from . import views
from django.urls import re_path, include

auths = SimpleRouter()
auths.register(r'auths', views.AuthViewSet)

locations = SimpleRouter()
locations.register(r'locations', views.LocationsViewSet)

locations_router = routers.NestedSimpleRouter(locations, r'locations', lookup='user')
locations_router.register(r'user_locations', views.UserLocationsViewSet)

records = SimpleRouter()
records.register(r'records', views.RecordsViewSet)

urlpatterns = [

    re_path(r'^', include(auths.urls)),

    re_path(r'^', include(locations.urls)),
    re_path(r'^', include(locations_router.urls)),

    re_path(r'^', include(records.urls)),

    re_path(r'^last_record/', views.LastRecordViewSet.as_view(dict(get='retrieve', put='update')))
]