from django.urls import path, include
from predict import views

urlpatterns = [
    path('predict', views.PredictView.as_view()),
]
