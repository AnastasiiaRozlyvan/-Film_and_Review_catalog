from django.urls import path
from .views import MovieCreateView
from .views import index
urlpatterns = [path('', index, name='index'),
               path('add/', MovieCreateView.as_view(), name='add'),
               ]
