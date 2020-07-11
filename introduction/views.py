from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'introduction/profile.html')

def drama(request):
    return render(request, 'introduction/drama.html')

def pictures(request):
    return render(request, 'introduction/pictures.html')

def music(request):
    return render(request, 'introduction/music.html')

def album(request):
    return render(request,'introduction/album.html')    
   
def cafe(request):
    return render(request,'introduction/youandi.html')   

def edam(request):
    return render(request,'introduction/edam.html')   
       
    
