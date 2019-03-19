from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Advertisement, Rubric
from .forms import AdvForm


def index(request):
    advs = Advertisement.objects.all()
    rubrics = Rubric.objects.all()
    context = {'advs': advs, 'rubrics': rubrics}
    return render(request, 'billboard/index.html', context=context)


def by_rubric(request, rubric_id):
    advs = Advertisement.objects.filter(rubric_id=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'advs': advs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'billboard/by_rubric.html', context)


class AdvCreateView(CreateView):
    template_name = 'billboard/create.html'
    form_class = AdvForm
    success_url = reverse_lazy('bboard:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
