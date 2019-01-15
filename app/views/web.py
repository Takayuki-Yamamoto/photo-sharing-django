from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.models import Photo


class TimeLineView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'html/app/timeline.html'
    queryset = Photo.objects.order_by('created_at').reverse().all()
