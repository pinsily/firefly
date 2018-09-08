from django.urls import path
from . import views

app_name = 'developenv'

urlpatterns = [
    path("", views.index, name="dev_index"),
    path("status", views.car_status, name="dev_status"),
    path("command", views.car_command, name='dev_command')
]
