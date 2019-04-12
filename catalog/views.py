from django.http import HttpResponse
from django.template import loader
from .models import Movie
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import BdForm


def index(request):
    template = loader.get_template('catalog/index.html')
    bbs = Movie.objects.order_by('-title')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))


class MovieCreateView(CreateView):
    template_name = 'catalog/create.html'
    form_class = BdForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
