from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from .models import Review

def index(request):
    # if request.method == 'POST':
    #     entered_name = request.POST['username']
    #     if entered_name == "":
    #         return render(request, "reviews/reviews.html", { 'has_error': True })
    #     return HttpResponseRedirect("/reviews/thanks")
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review_query_set = Review(user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating'])
            review_query_set.save()
            # OR if we define modelForm we can directly use 
            # form.save() --> it will automatically save all the fields as we have already defined everything in the forms.py ReviewForm applicable for create an update
            return HttpResponseRedirect("/reviews/thanks")
        else:
            return render(request, "reviews/reviews.html", { 'form': form })
    return render(request, "reviews/reviews.html", { 'form': forms.ReviewForm() })


def thanks(request):
    return render(request, "reviews/thanks.html")

    