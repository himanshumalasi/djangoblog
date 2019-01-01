from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def index(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/index.html',context)




