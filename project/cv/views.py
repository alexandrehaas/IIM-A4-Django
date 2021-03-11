from django.shortcuts import render

def index(request):
    return render(request, 'cv/index.html')

def view(request):
    return render(request, 'cv/view.html')