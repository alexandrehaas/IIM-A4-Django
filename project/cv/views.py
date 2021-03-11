from django.shortcuts import render
from .models import ApplicantForm

def index(request):
    return render(request, 'cv/index.html')

def view(request):
    return render(request, 'cv/view.html')

def upload(request):
    context = {'applicant_form': ApplicantForm}
    return render(request, 'cv/upload.html', context)