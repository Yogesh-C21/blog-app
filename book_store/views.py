from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    # return HttpResponse(books)
    return render(request, 'book_store/index.html', { "books" : books})

def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
        # <Method 2> book = get_object_or_404(Book, id=id)
        return render(request, 'book_store/book_detail.html', {
            "title" : book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestselling": book.is_bestselling,
        })
    except:
        raise Http404()