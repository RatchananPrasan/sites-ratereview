from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .forms import CreateBookForm
from .models import *
from .validateFormatTools import VFBookTool
# Create your views here.



def createNewBook(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST,request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            input_ISBN = form.cleaned_data['isbn']
            input_book_name = form.cleaned_data['book_name']
            input_author_name = form.cleaned_data['author']
            input_genre = form.cleaned_data['genre']
            input_book_cover = form.cleaned_data['book_cover']
            wizard = VFBookTool()
            if wizard.validateISBN(input_ISBN):
                input_ISBN = wizard.formatISBN(input_ISBN)
                try:
                    book = Book.objects.get(isbn = input_ISBN)
                    #return render(request, 'books/create_book.html',{'form':form,'error':'Book with the following ISBN already exist'})
                    return redirect('books:book_detail',book.id)
                except Book.DoesNotExist:
                    try:
                        input_author_name = wizard.formatAuthorName(input_author_name)
                        writer = Author.objects.get(author_name = input_author_name )
                    except Author.DoesNotExist:
                        writer = Author(author_name = input_author_name)
                        writer.save()
                    #CreateBook
                    newBook = Book(isbn = input_ISBN, book_name = input_book_name, author = writer, genre = input_genre, book_cover = input_book_cover, booked_by = request.user )
                    newBook.save()
                    
                    return redirect('books:book_detail',newBook.id)
                
            else:
                form = CreateBookForm()
                return render(request, 'books/create_book.html',{'form':form,'error':'ISBN must contain only number'})
            
    form = CreateBookForm()
    #return render(request, 'books/create_book.html',{'form':form})
    return render(request, 'books/createBook.html',{'form':form})


def get_book_detail(request,book_id):
    book = get_object_or_404(Book, pk = book_id)
  
        
    
    try:
        ## get post
        ratedPost = BookRating.objects.filter(book = book.id).order_by('-pub_date')
        print('\t\t',ratedPost)
        return render(request,'books/book_detail.html',{'book':book,'ratedPost':ratedPost})
    except:
        return render(request,'books/book_detail.html',{'book':book,'ratedPost':None})


def searching(request):
    s = request.GET['search_key']
    sk = "+".join(s.split())
    if sk != '':
        return redirect('books:book_search',sk)
    else:
        books = Book.objects.all()
        return render(request, 'books/browse_page.html',{'books':books})
    

def searchBook(request,search_key):
    search_key = " ".join(search_key.split('+'))
    books = Book.objects.filter(book_name__icontains =  search_key)| Book.objects.filter(author__author_name__icontains = search_key)
    return render(request, 'books/browse_page.html',{'books':books, 'book_found':len(books)})


def browseAllBooks(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'books/browse_page.html',{'books':books, 'book_found':len(books)})


def createNewBookRating(request,book_id):
      
    if request.method == 'POST':      
        print('\tin')
        try:
            rating = request.POST.get('rated_score')
            if rating is None:
                raise ValueError
            comment = request.POST.get('comment')
            
            print(rating,"star")
            print(comment)
            print(request.user)
            book = Book.objects.get(pk = book_id)
            newBookRate = BookRating(rate = rating, description = comment, book = book ,booked_by = request.user)
            newBookRate.save()
            
            
        except ValueError:
            print('\t\terror')
            pass
        
    return redirect('books:book_detail',book_id)
        

                                
