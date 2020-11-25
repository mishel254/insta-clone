from django.shortcuts import render
from .models import Users,Post,Bio

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def  instagram(request):
    user = Users.objects.all()
    posts = Post.objects.all()
    context = {'posts':posts,'user':user}
    return render (request,'interface.html',context)

def profile(request):
    username =  User.objects.all()
    context = {'username':username}
    return render(request,'profile.html',context)
