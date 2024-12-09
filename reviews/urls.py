from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("class-based", views.ReviewView.as_view()),
    path("thanks", views.thanks),
]
