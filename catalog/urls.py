from django.urls import path
from .views import MovieCreateView
from .views import index, statistics, InfoView
urlpatterns = [path('', index, name='index'),
               path('add/', MovieCreateView.as_view(), name='add'),
               path('statistics/', statistics, name='statistics'),
               path('movie/<int:pk>', InfoView.as_view(), name='movie_info'),
]


