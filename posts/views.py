from django.shortcuts import render, redirect, get_object_or_404
from .models import *
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

def show(request, id):
    post = get_object_or_404(Post, pk=id)
    post.view_count = post.view_count +1
    post.save()
    all_comments = post.comments.all().order_by('-created_at')  ### -는 내림차순
    return render(request, 'posts/show.html', {"post":post, 'comments':all_comments}) 


def update(request, id):   
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('posts:show', post.id)
    return render(request, 'posts/edit.html', {'post':post})

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('posts:main')

def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk = post_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, user= current_user, post= post)
        ########## if가 실행 될 때
    return redirect('posts:show', post.pk)    ##앱 이름 : show로! >>post.pk를 같이 갖고 간다.
    
    ####### post가 아닐 경우에도 실행됨


