from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendmessage', views.send_message, name='send_message')
]
