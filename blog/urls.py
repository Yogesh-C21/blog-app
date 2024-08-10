"""Module providing a function printing python version."""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("posts", views.post, name="posts"),
    path("posts/<slug>", views.post_detail, name="post-detail")
]
