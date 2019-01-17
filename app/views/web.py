from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.models import Photo


class TimeLineView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'app/timeline.html'
    queryset = Photo.objects.order_by('created_at').reverse().all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TimeLineView, self).get_context_data(**kwargs)
        print("*****************************************")
        print(dict(context))
        return context


class SlideShowView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'app/slideshow.html'
    queryset = Photo.objects.order_by('created_at').reverse().all()
