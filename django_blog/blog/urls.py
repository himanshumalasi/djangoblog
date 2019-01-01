from django.urls import path
from .views import home,index

urlpatterns = [
    path('',home,name="blog-home"),
    path('index/',index,name="blog-index")
]
