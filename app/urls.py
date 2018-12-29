from django.urls import path

from .views import api, web

app_name='app'
urlpatterns = [
    path('', web.PhotoListView.as_view(), name="index"),
    path('callback', api.callback, name="callback"),
]