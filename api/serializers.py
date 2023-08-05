
from rest_framework import serializers
from books.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    
    book_img = serializers.SerializerMethodField()

    def get_book_img(self, obj):                            # obj - objects
        return f"http://127.0.0.1:8000{obj.book_img.url}"

    class Meta:
        model = BookModel
        fields = "__all__"

