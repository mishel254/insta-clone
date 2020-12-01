from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Users,Post,Bio,like,Profiles
from .forms import  CreateUserForm
from django.contrib import messages

# Create your views here.
def signin(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created for ' + User)
            return redirect('login')
        
    context = {'form':form}
    return render(request,'registration/registration_form.html',context)
     
def login(request):
    form=CreateUserForm()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_admin==False:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('interface')
    context = {'form':form}
    return render (request,'registration/login.html',context)


@login_required
def instagram(request):
    qs = Post.objects.all()
    user = request.user

    context = {'qs':qs,'user':user}
    return render(request,'gram.html',context)

def profile(request):
    profile=Profiles.objects.get(user=request.user)

    context = {'profile':Profile}
    return render(request,'profile.html',context)



def likes(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id = post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        likes = like.objects.get-or_create(user=user,post_id=post_id)
        likes.save()

    return redirect('clone:interface')



def logout(request):
    return redirect('login')



