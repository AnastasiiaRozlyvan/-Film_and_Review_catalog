from django.forms import ModelForm
from .models import Movie, MovieDescription, Cast, Staff


class MovieAddingForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'directed_by', 'year', 'genre', )


class MovieDescriptionAddingForm(ModelForm):
    class Meta:
        model = MovieDescription
        fields = ('movie', 'synopsis', 'rate', )


class ActorAddingForm(ModelForm):
    class Meta:
        model = Cast
        fields = ('movie', 'role', 'name',)


class CrewAddingForm(ModelForm):
    class Meta:
        model = Staff
        fields = ('movie', 'position', 'name',)
