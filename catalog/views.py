from django.http import HttpResponse
from .models import Bd
def index(request) :
    s = "Here will be film and review catalog.\r\n"
    for bb in Bd.objects.order_by('-title'):
        s += bb.title  + bb.content
    return HttpResponse(s)
