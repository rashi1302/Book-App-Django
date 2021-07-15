import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Book
        fields = ['book_genre', 'book_lang']