from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_genre = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50, blank=True)
    book_lang = models.CharField(max_length=50, default="English")
    book_year = models.IntegerField()

    def __str__(self):
        return self.book_name