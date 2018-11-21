# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Filename：      urls
   Author :        pinsily
   date：          18.11.16 16:16
   Description :
-------------------------------------------------
"""
from django.urls import path

from fireadmin import views

app_name = "fireadmin"

urlpatterns = [
    path('', views.index, name="index"),
    path('typography/', views.typography, name='typography'),
    path('content_widgets/', views.content_widgets, name="content_widgets"),
    path('tables/', views.tables, name="tables"),
    path('form_elements/', views.form_elements, name="form_elements"),
    path('form_components/', views.form_components, name="form_components"),
    path('form_examples/', views.form_examples, name="form_examples"),
    path('form_validation/', views.form_validation, name="form_validation"),
    path('buttons/', views.buttons, name="buttons"),
    path('labels/', views.labels, name="labels"),
    path('images_icons/', views.images_icons, name="images_icons"),
    path('alerts/', views.alerts, name="alerts"),
    path('media/', views.media, name="media"),
    path('components/', views.components, name="components"),
    path('other_components/', views.other_components, name="other_components"),
    path('charts/', views.charts, name="charts"),
    path('file_manager/', views.file_manager, name="file_manager"),
    path('calendar/', views.calendar, name="calendar"),
    path('list_view/', views.list_view, name="list_view"),
    path('profile_page/', views.profile_page, name="profile_page"),
    path('messages/', views.messages, name="messages"),
    path('login/', views.login, name="login"),
    path('notfound/', views.notfound, name="notfound"),
    path('commands/', views.commands, name='commands'),
]
