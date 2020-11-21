from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def  instagram(request):
    return render (request,'interface.html')