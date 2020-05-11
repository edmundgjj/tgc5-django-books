from django import forms
from .models import Book, Genre


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'desc', 'ISBN', 'genre', 'tags', 'owner', 'photo')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False)
