from django import forms

class CreateBookForm(forms.Form):
    isbn = froms.charField(label = 'ISBN:', max_length = 13)
    book_name = forms.CharField(label = 'Book Name', max_length = 50)
    author = author_name = models.CharField(label = 'author_name', max_length = 50)
