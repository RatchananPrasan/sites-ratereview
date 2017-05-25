from django.db import models
from django.db.models import Avg
from accounts.models import User
from django.utils import timezone



# Create your models here.       

class Author(models.Model):
    author_name = models.CharField(max_length = 50)

class Book(models.Model):
    GENRE = (('arts','Arts & Photography'),('biographies','Biographies & Memoirs'),('children','Children\'s Books'),('histosy','History'),('literature','Literature & Fiction'),('mystery','Mystery & Suspense'), ('romance','Romance'),('sci-fi','Sci-Fi & Fiction'),('teens','Teens & Young Adult'),('textbook','Textbooks'),('other','Other'))
    isbn = models.CharField(max_length = 13)
    book_name = models.CharField(max_length = 50)
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    genre = models.CharField(max_length = 20, choices = GENRE, default = ('other','Other'))
    book_cover = models.ImageField(upload_to = 'media/books/book_cover',default = 'media/books/book_cover/no_cover.jpg')
    
    booked_by = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'booked_by')
    
    def getRating(self):
        rating = BookRating.objects.filter(book = self.id).aggregate(Avg('rate'))
        rate = rating['rate__avg']
        if rate == None:
            rate = 0
        return rate


class BookRating(models.Model):
    RATE = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rate = models.IntegerField(choices = RATE)
    description = models.TextField()
    book = models.ForeignKey(Book,on_delete = models.CASCADE)
    booked_by = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'booked_rated_by')
    pub_date = models.DateTimeField(default=timezone.now)

