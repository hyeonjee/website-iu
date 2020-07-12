from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def new(request):
    form = PostForm()
    context = {
        'form':form
    }
    return render(request, 'posts/new.html', context)

def create(request):   
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
    return redirect('posts:main')

def main(request):
    context = {
        'posts' : Post.objects.all().order_by('-created_at')
    }
    return render(request, 'posts/main.html', context)    

def show(request, id) :
    post = Post.objects.get(pk=id)
    return render(request, 'posts/show.html', {'post':post}) 