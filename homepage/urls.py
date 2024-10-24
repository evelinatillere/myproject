from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("form/", views.form_view, name="form"),
    path("git/", views.git_view, name="git"),
    path("send_email/", views.send_email_view, name='send_email'),
]