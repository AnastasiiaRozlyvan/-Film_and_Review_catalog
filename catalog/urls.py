from django.urls import path
from .views import MovieCreateView, CommentCreateView
from .views import index, statistics
urlpatterns = [path('', index, name='index'),
               path('add/', MovieCreateView.as_view(), name='add'),
               path('comment/', CommentCreateView.as_view(), name='comment'),
               path('statistics/', statistics, name='statistics'),

               ]
