from django.forms import ModelForm
from .models import Movie, Comments


class MovieAddingForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'content', 'year')


class CommentAddingForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
