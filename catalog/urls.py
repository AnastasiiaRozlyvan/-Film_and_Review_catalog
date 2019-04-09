from django.urls import path
from .views import BdCreateView
from .views import index
urlpatterns = [path('', index, name='index'),
               path('add/', BdCreateView.as_view(), name='add'), ]
