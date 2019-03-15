from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from conference.models import Talk


def speaker(request):
    return render(request, 'conference/speaker.html')


class TalkList(ListView):
    model = Talk


class TalkView(DetailView):
    model = Talk


class TalkCreate(CreateView):
    model = Talk
    fields = ('title', 'description')
    success_url = reverse_lazy('talk_list')


class TalkUpdate(UpdateView):
    model = Talk
    fields = ('title', 'description')
    success_url = reverse_lazy('talk_list')


class TalkDelete(DeleteView):
    model = Talk
    success_url = reverse_lazy('talk_list')
