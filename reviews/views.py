from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ReviewForm
from .models import Review


def show_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/show_reviews.template.html', {
        'reviews': reviews
    })


def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        # create an instance of review, but don't commit, so that we have a chance to set the user
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        messages.success(request, "New review has been added - " + review.title)
        return redirect(reverse(show_reviews))
    else:
        form = ReviewForm()

    return render(request, 'reviews/create_review.template.html', {
        'form': form
    })