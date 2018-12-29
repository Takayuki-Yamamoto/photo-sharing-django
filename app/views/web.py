from django.views.generic import ListView

from app.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'html/app/index.html'
