from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path('users_page/', views.users_page, name="users_page"),
    path('books/', views.books, name='books'),
    path('users/<int:user_id>', views.user, name='user'),
    path('books/<int:book_id>', views.book, name='book'),
]