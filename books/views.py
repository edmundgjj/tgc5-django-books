from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book, Genre
from .forms import BookForm, SearchForm
from reviews.forms import ReviewForm


# Create your views here.
def index(request):
    books = Book.objects.all()

    # if there is any GET queries
    print(request.GET)
    if request.GET:
        # always true query:
        queries = ~Q(pk__in=[])

        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            queries = queries & Q(title__icontains=title)

        if 'genre' in request.GET and request.GET['genre']:
            print("adding genre")
            genre = request.GET['genre']
            queries = queries & Q(genre__id__in=genre)

        books = books.filter(queries)

    genres = Genre.objects.all()
    search_form = SearchForm(request.GET)

    return render(request, 'books/index.template.html', {
        'books': books,
        'genre': genres,
        'search_form': search_form
    })


def view_book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    review_form = ReviewForm()
    return render(request, 'books/details.template.html', {
        'book': book,
        'form': review_form
    })


def create_book(request):
    if request.method == 'POST':
        create_form = BookForm(request.POST)

        # check if the form has valid values
        if create_form.is_valid():
            book = create_form.save()
            messages.success(request, f"New book {book.title} has been created")
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
