from django.db import models

# Create your models here.       

class Author(models.Model):
    author_name = models.CharField(max_length = 50)

class Book(models.Model):
    GENRE = ('fiction','non-fiction', 'other')
    isbn = models.CharField(max_length = 13, primary_key = True)
    book_name = models.CharField(max_length = 50)
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    #genre = models.CharField(max_length = 20, choices = GENRE)


