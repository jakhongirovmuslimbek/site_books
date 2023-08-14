from django.urls import path
from .views import *

urlpatterns = [
    path('category_all/', CategoryView.as_view()),
    path('books_all/', BooksView.as_view()),
    path('user_create/', UserView.as_view()),

    path('by_category_id/<int:id>/', by_category_id),
    path('book_id/<int:pk>/', BookIDView.as_view()),
]
