from django.urls import path
from .views import BookAPIView1, TypeView


app_name = 'users'

urlpatterns = [
    path('apibook1/', BookAPIView1.as_view(), name='book1'),
    path('api/type/', TypeView.as_view(), name='type')
]

