from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'incoming/index.html')

def add(request):
    return render(request, 'incoming/add.html')

def show(request):
    return render(request, 'incoming/show.html')

def edit(request):
    return render(request, 'incoming/edit.html')

def search(request):
    return render(request, 'incoming/index.html')
