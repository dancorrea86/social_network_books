from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path('users_page/', views.users_page, name="users_page"),
    path('books_page/', views.books_page, name='books_page'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('book/<int:book_id>/', views.book, name='book'),
]