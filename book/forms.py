from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Book

class Bookform(ModelForm):
    class Meta:
        model=Book
        fields=('book_name','book_lang','book_genre','book_year','book_author')

        widgets={
            'book_name':forms.TextInput(attrs={'class':"form-control"}),
            'book_author':forms.TextInput(attrs={'class':"form-control"}),
            'book_lang':forms.TextInput(attrs={'class':"form-control"}),
            'book_genre':forms.TextInput(attrs={'class':"form-control"}),
            'book_year':forms.TextInput(attrs={'class':"form-control"})
            

        }
