from django.views.generic import ListView

from app.models import PhotoUrl


class PhotoListView(ListView):
    model = PhotoUrl
    template_name = 'html/app/index.html'
