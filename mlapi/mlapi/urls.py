from django.urls import path, include

API_V1 = 'api/v1/'

urlpatterns = [
    path(API_V1, include('features.urls')),
]
