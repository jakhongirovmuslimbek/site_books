from django.urls import path
from .views import *

urlpatterns = [
    path('category_all/', CategoryView.as_view()),
    path('books_all/', BooksView.as_view()),

]