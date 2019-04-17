from django.http import HttpResponse
from django.template import loader
from .models import Movie, MovieDescription
from .models import Cast
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .forms import MovieAddingForm, CommentAddingForm


def index(request):
    template = loader.get_template('catalog/index.html')
    descr = MovieDescription.objects.all()
    context = {'descriptions': descr}
    return HttpResponse(template.render(context, request))


def statistics(request):
    template = loader.get_template('catalog/statistics.html')
    num_films = Movie.objects.all().count()
    num_actors = Cast.objects.all().count()
    context = {
        'num_films': num_films,
        'num_actors': num_actors,
            }
    return HttpResponse(template.render(context, request))


class MovieCreateView(CreateView):
    template_name = 'catalog/create.html'
    form_class = MovieAddingForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CommentCreateView(CreateView):
    template_name = 'catalog/comment.html'
    form_class = CommentAddingForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InfoView(DetailView):
    template_name = 'catalog/movie_info.html'
    model = MovieDescription
    context_object_name = 'MovieDescription'
