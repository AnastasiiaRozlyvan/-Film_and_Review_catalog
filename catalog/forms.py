from django.forms import ModelForm
from .models import Movie
class BdForm(ModelForm):


    class Meta:
        model = Movie
        fields = ('title', 'content')