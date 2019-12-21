from rest_framework import serializers
from .models import UserProfile, Book, Type


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        #fields = "__all__"
        fields = ('title', 'isbn', 'rate', 'auther')


class TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
