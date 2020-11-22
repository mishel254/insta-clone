from django.shortcuts import render
from .models import User,Post,Bio

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def  instagram(request):
    username = User.objects.all()
    context = {'username':username}
    return render (request,'interface.html',context)