from django.urls import path

from .views import api, web

app_name='app'
urlpatterns = [
    path('', web.TimeLineView.as_view(), name="timeline"),
    path('callback', api.callback, name="callback"),
]