from rest_framework import serializers
from .models import UserProfile, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        #fields = "__all__"
        fields = ('title', 'isbn', 'rate', 'auther')
