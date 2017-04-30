from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CreateBookForm

# Create your views here.


def get_book_name(request):
    # if this is a POST request we need to process the form data
    if request.methis == 'POST':
        # creatr e a form instance and populate it with data from the request:
        form = CreateBookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #process the data in form.cleaned_Data as required
            #...
            #redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        else:
            form = BookForm()
        return render(request, 'create_book.html', {'form': form})
