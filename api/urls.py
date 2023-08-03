from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('category_all/', CategoryView.as_view()),
    
]