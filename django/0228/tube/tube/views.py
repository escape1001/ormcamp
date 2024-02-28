from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Video, Comment, Like, Tag
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class TubeList(ListView):
    model = Video
    ordering = "-pk"

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q', '')

        if q :
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(contents__icontains=q)
            ).distinct()

        return queryset
    

class TubeDetail(DetailView):
    model = Video


class TubeCreate(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'contents', 'thumbnail_image', 'video_upload', 'tags']
    success_url = reverse_lazy('tube_list')

    def form_valid(self, form):
        video = form.save(commit=False)
        video.author = self.request.user
        return super().form_valid(form)


class TubeUpdate(UserPassesTestMixin, UpdateView):
    model = Video
    fields = ['title', 'contents', 'thumbnail_image', 'video_upload', 'tags']

    def get_success_url(self):
        return reverse('tube_detail', args=[str(self.object.pk)])
    
    def test_func(self):
        return self.request.user == self.get_object().author


class TubeDelete(UserPassesTestMixin, DeleteView):
    model = Video
    success_url = reverse_lazy('tube_list')

    def test_func(self):
        return self.request.user == self.get_object().author


# class TubeTagList():
#     pass


tube_list = TubeList.as_view()
tube_detail = TubeDetail.as_view()
tube_create = TubeCreate.as_view()
tube_update = TubeUpdate.as_view()
tube_delete = TubeDelete.as_view()
# tube_tag_list = TubeTagList