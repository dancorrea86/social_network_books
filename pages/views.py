from django.views.generic import TemplateView
from django.shortcuts import render



def home(request):
    return render(request, "pages/home.html")

def users_page(request):
    return render(request, "pages/users_page.html")

def books(request):
    return render(request, "pages/books.html")

def book(request, book_id):
    return render(request, "pages/book_profile.html")

def user(request, user_id):
    return render(request, "pages/user_profile.html")

def register(request):
    return render(request, "pages/register.html")
    
