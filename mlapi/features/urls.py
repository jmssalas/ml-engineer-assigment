from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from features import views

urlpatterns = (
    path('features', views.FeatureCreate.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
