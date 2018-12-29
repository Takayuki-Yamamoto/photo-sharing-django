from django.views.generic import ListView

from app.models import PhotoUrl


class PhotoListView(ListView):
    model = PhotoUrl
    template_name = 'html/app/index.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     return super().get_context_data()