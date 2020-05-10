from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from books.models import Book


def show_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/show_reviews.template.html', {
        'reviews': reviews
    })


def create_review(request, book_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        # create an instance of review, but don't commit, so that we have a chance to set the user
        review = form.save(commit=False)
        review.user = request.user
        review.book = get_object_or_404(Book, pk=book_id)
        review.save()
        messages.success(request, "New review has been added - " + review.title)
        return redirect(reverse('view_reviews_route'))
    else:
        form = ReviewForm()

    return render(request, 'reviews/create_review.template.html', {
        'form': form
    })