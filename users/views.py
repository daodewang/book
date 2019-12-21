from django.shortcuts import render

from .serializers import BookSerializer, TypeModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile, Book, Type
from rest_framework.renderers import JSONRenderer
# Create your views here.

class BookAPIView1(APIView):
    def get(self, request, format=None):
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIKey=APIKey).first()
        if developer:
            balance = developer.money
            if balance>0:
                isbn = self.request.query_params.get('isbn', 0)
                books = Book.objects.filter(isbn=int(isbn))
                books_serializer = BookSerializer(books, many=True)
                developer.money -= 1
                developer.save()
                return Response(books_serializer.data)
            else:
                return Response('兄弟，你该充钱了啦！')
        else:
            return Response('查无此人啊')


class TypeView(APIView):
    """
    操作类别表
    """
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        types = Type.objects.all()
        types_serializer = TypeModelSerializer(types, many=True)
        return Response(types_serializer.data)

    def post(self, request):
        name = request.data.get('name')
        category_type = request.data.get('lei')
        parent_category_id = request.data.get('parent')
        type = Type()
        type.name = name
        type.category_type = category_type
        if parent_category_id:
            parent_category = Type.objects.filter(id=parent_category_id).first()
            type.parent_category = parent_category

        type.save()
        type_serializer = TypeModelSerializer(type)
        return Response(type_serializer.data)
