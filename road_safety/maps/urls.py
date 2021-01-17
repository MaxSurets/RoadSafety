from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.geojson_by_zip.as_view(), name = 'zip'),
    path('location/', views.location_from_zip.as_view(), name = 'location')
]