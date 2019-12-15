from django.urls import path
from .views import BookAPIView1


app_name = 'users'

urlpatterns = [
    path('apibook1/', BookAPIView1.as_view(), name='book1')
]

