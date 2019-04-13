from django.forms import ModelForm
from .models import Movie, Comments


class MovieAddingForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'directed_by', 'year', 'genre', )


class CommentAddingForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
