from django.http import HttpResponse
from django.template import loader
from .models import Movie, MovieDescription, Cast
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from .forms import MovieAddingForm
from django.db.models import Avg
from django_comments.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class MovieList(ListView):
    template_name = 'catalog/index.html'
    model = MovieDescription
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        descr = MovieDescription.objects.all()
        context['descriptions'] = {'descriptions': descr}
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return MovieDescription.objects.filter(Q(movie__title__icontains=query) |
                                                   Q(movie__year__icontains=query) |
                                                   Q(movie__genre__icontains=query) |
                                                   Q(movie__directed_by__icontains=query) |
                                                   Q(synopsis__icontains=query))
        else:
            return MovieDescription.objects.all()


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


class MovieCreateView(LoginRequiredMixin, CreateView):
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
