from django.http import HttpResponse
from django.template import loader
from .models import Movie, MovieDescription
from .models import Cast
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .forms import MovieAddingForm
from django.db.models import Avg
from django_comments.models import Comment


def index(request):
    template = loader.get_template('catalog/index.html')
    descr = MovieDescription.objects.all()
    context = {'descriptions': descr}
    return HttpResponse(template.render(context, request))


def statistics(request):
    template = loader.get_template('catalog/statistics.html')
    num_films = Movie.objects.all().count()
    num_actors = Cast.objects.all().count()
    comment_count = Comment.objects.all().count()
    av_rate = MovieDescription.objects.all().aggregate(Avg('rate'))
    context = {
        'num_films': num_films,
        'num_actors': num_actors,
        'av_rate': av_rate['rate__avg'],
        'comment_count': comment_count,
            }
    return HttpResponse(template.render(context, request))


class MovieCreateView(CreateView):
    template_name = 'catalog/create.html'
    form_class = MovieAddingForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InfoView(DetailView):
    template_name = 'catalog/movie_info.html'
    model = MovieDescription
    context_object_name = 'MovieDescription'
