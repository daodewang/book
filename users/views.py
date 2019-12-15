from django.shortcuts import render

from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile, Book
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
