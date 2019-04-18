from django.forms import ModelForm
from .models import Movie


class MovieAddingForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'directed_by', 'year', 'genre', )
