from django.shortcuts import render, redirect, get_object_or_404
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
        image = request.FILES.get('image')
        user = request.user
        Post.objects.create(title=title, content=content, image=image, user=user)
    return redirect('posts:main')

def main(request):
    context = {
        'posts' : Post.objects.all().order_by('-created_at')
    }
    return render(request, 'posts/main.html', context)    

def show(request, id) :
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/show.html', {'post':post}) 


def update(request, id):   
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('posts:show', post.id)
    return render(request, 'posts/update.html', {'post':post})

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("posts:main")
