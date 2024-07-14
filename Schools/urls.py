from django.urls import path

from Schools.views import hello,index
urlpatterns = [
     path('hello', hello,name='helloworld'),
     path('index/<int:id>', index,name='index.html'),
]
