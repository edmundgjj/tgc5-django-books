from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
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


def update_book(request, book_id):
    # 1. retrieve the book that we are editing
    book_being_updated = get_object_or_404(Book, pk=book_id)

    # 2. if the update form is submitted
    if request.method == "POST":

        # 3. create the form and fill in the user's data. Also specify that
        # this is to update an existing model (the instance argument)
        book_form = BookForm(request.POST, instance=book_being_updated)
        if book_form.is_valid():
            book_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'books/update.template.html', {
                "form": book_form
            })
    else:
        # 4. create a form with the book details filled in
        book_form = BookForm(instance=book_being_updated)
        return render(request, 'books/update.template.html', {
            "form": book_form
        })


def delete_book(request, book_id):
    book_to_delete = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book_to_delete.delete()
        return redirect(index)
    else:
        return render(request, 'books/delete_book.template.html', {
            "book": book_to_delete
        })
