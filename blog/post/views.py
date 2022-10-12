from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Post
from . models import Contact
from . forms import PostForm, CustomFormUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index(request):
    post={
        'post':Post.objects.all()
    }
    return render(request,'index.html',post)
    
def author(request):
    return render(request,'author.html')
    
def category1(request):
    return render(request,'category1.html')
    
def category2(request):
    return render(request,'category2.html')
    
def category3(request):
    return render(request,'category3.html')
    
def contacts(request):
    contact={
        'contact':Contact.objects.all()
    }
    return render(request,'contact.html',contact)
    
@login_required    
def single(request):
    form=PostForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Order Successful. Thank You...</h1>')
    post={
        'form':form
        }
    return render(request,'single.html',post)

def register(request):
    form=CustomFormUserCreationForm()
    if request.method=='POST':
        form=CustomFormUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Registration Successful. Thank You...</h1>')
    return render(request,'register.html',{'form':form})