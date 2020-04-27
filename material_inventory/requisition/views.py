from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'requisition/index.html')

def add(request):
    return render(request, 'requisition/add.html')

def show(request):
    return render(request, 'requisition/show.html')

def edit(request):
    return render(request, 'requisition/edit.html')

def search(request):
    return render(request, 'requisition/index.html')