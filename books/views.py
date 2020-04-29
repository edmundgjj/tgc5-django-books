from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.template.html', {
        'books': books
    })


def create_book(request):
    if request.method == 'POST':
        create_form = BookForm(request.POST)

        # check if the form has valid values
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            # if does not have valid values, re-render the form
            return render(request, 'books/create.template.html', {
                'form': create_form
            })
    else:
        create_form = BookForm()
        return render(request, 'books/create.template.html', {
            'form': create_form
        })
