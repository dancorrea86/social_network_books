from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from .models import Book
from users.models import User



def home(request):
    return render(request, "pages/home.html")


def users_page(request):
    users = User.objects.all()
    dados = {
        'users': users
    }
    return render(request, "pages/users_page.html", {'users': users})


def books_page(request):
    books = Book.objects.all()
    dados = {
        'books': books
    }
    return render(request, "pages/books_page.html", {'books': books})


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "pages/book_profile.html", {'book': book})

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "pages/user_profile.html", {'user': user})


def register(request):
    return render(request, "pages/register.html")
    
