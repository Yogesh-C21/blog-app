from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, "blog/index.html")

def post():
    pass

def post_detail():
    pass