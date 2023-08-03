
from .serializers import CategorySerializer
from books.models import CategoryModel
from rest_framework.views import APIView
from rest_framework import status
from rest_framework .response import Response


class CategoryView(APIView):

    def get(self, request):
        category = CategoryModel.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
