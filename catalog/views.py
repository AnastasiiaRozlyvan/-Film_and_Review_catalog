from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Movie
from .models import Cast
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import MovieAddingForm, CommentAddingForm


def index(request):
    template = loader.get_template('catalog/index.html')
    movies = Movie.objects.order_by('-title')
    context = {'movies': movies}
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
