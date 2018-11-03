from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .forms import *
from .models import *
from .validateFormatTools import VFBookTool

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
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
    books = Book.objects.filter(book_name__icontains = search_key)|Book.objects.filter(author__author_name__icontains = search_key)  
    return render(request, 'books/browse_page.html',{'books':books, 'book_found':len(books)})

def searchByGenre(request,search_key):
    gen = search_key
    books = Book.objects.filter(genre = gen)
    return render(request, 'books/browse_page.html',{'books':books, 'book_found':len(books)})


def browseAllBooks(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'books/browse_page.html',{'books':books, 'book_found':len(books)})


def createNewBookRating(request,book_id):
      
    if request.method == 'POST':      
        try:
            rating = request.POST.get('rated_score')
            if rating is None:
                raise ValueError
            comment = request.POST.get('comment')
            book = Book.objects.get(pk = book_id)
            newBookRate = BookRating(rate = rating, description = comment, book = book ,booked_by = request.user)
            newBookRate.save()
            
        except ValueError:
            pass
        
    return redirect('books:book_detail',book_id)


def deleteBook(request,book_id):
    book = Book.objects.get(pk = book_id)
    book.delete()
    return redirect('books:browse_all_book')

    
def editBook(request,book_id):
    if request.method == 'POST':
        form = CreateBookForm(request.POST,request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            input_ISBN = form.cleaned_data['isbn']
            input_book_name = form.cleaned_data['book_name']
            input_author_name = form.cleaned_data['author']
            input_genre = form.cleaned_data['genre']
            input_book_cover = form.cleaned_data['book_cover']
            book = Book.objects.get(pk = book_id)
            wizard = VFBookTool()
            if wizard.validateISBN(input_ISBN):
                input_ISBN = wizard.formatISBN(input_ISBN)
                try:
                    input_author_name = wizard.formatAuthorName(input_author_name)
                    writer = Author.objects.get(author_name = input_author_name )
                except Author.DoesNotExist:
                    writer = Author(author_name = input_author_name)
                    writer.save()

                return redirect('books:book_detail',book.id)

            else:
                form = EditBookForm()
                return render(request, 'books/EditBook.html',{'form':form,'error':'ISBN must contain only number'})

    form = EditBookForm()
    book = Book.objects.get(pk = book_id)
    return render(request, 'books/EditBook.html',{'form':form,'book':book})

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == "GET":
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == "GET":
        author = Author.objects.all()
        serializer = BookSerializer(author, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def bookrate_list(request):
    if request.method == "GET":
        bookrate = BookRating.objects.all()
        serializer = BookSerializer(bookrate, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)