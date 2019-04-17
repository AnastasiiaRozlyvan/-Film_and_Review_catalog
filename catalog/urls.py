from django.urls import path
from .views import MovieCreateView, CommentCreateView
from .views import index, statistics, InfoView
urlpatterns = [path('', index, name='index'),
               path('add/', MovieCreateView.as_view(), name='add'),
               path('comment/', CommentCreateView.as_view(), name='comment'),
               path('statistics/', statistics, name='statistics'),
               path('movie/<int:pk>', InfoView.as_view(), name='movie_info'),
]


