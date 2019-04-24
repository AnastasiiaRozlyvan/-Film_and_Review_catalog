from django.urls import path
from .views import MovieCreateView, MovieDescrCreateView, ActorAddView, CrewAddView
from .views import MovieList, statistics, InfoView
urlpatterns = [path('', MovieList.as_view(), name='index'),
               path('add/', MovieCreateView.as_view(), name='add'),
               path('add_description/', MovieDescrCreateView.as_view(), name='add_description'),
               path('add_actor/', ActorAddView.as_view(), name='add_actor'),
               path('add_crew/', CrewAddView.as_view(), name='add_crew'),
               path('statistics/', statistics, name='statistics'),
               path('movie/<int:pk>', InfoView.as_view(), name='movie_info'),
]


