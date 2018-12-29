from django.urls import path

from .views import api, web

urlpatterns = [
    path('', web.index, name="index"),
    path('callback', api.callback, name="callback"),
]