
from .serializers import *
from books.models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view

class CategoryView(APIView):
    def get(self, request):
        category = CategoryModel.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class BooksView(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# for users only
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 09.08.2023
@api_view(['GET'])
def by_category_id(request, id):
    by_category = BookModel.objects.filter(category_id=id)
    if by_category:
        serializer = BookSerializer(by_category, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Category information was not found'}, status=status.HTTP_404_NOT_FOUND)

class BookIDView(APIView):
    def get(self, request, pk):
        book = BookModel.objects.filter(id=pk) 
        if book:
            serializer = BookSerializer(book, many=True)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Book ID was not found!'}, status=status.HTTP_404_NOT_FOUND)


