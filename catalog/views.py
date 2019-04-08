from django.http import HttpResponse
from django.template import loader
from .models import Bd
def index(request) :
    template = loader.get_template('catalog/index.html')
    bbs = Bd.objects.order_by('-title')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
