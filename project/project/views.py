from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'project/index.html')

def blockchainTeam(request):
    return render(request, 'project/blockchain-team.html')

def databasesTeam(request):
    return render(request, 'project/databases-team.html')

def graphicTeam(request):
    return render(request, 'project/graphic-team.html')

def IATeam(request):
    return render(request, 'project/ia-team.html')

def objectsTeam(request):
    return render(request, 'project/objects-team.html')

def softwaresTeam(request):
    return render(request, 'project/softwares-team.html')

def about(request):
    return render(request, 'project/about.html')

def contact(request):
    return render(request, 'project/contact.html')

def cv(request):
    return render(request, 'project/cv.html')

def viewCv(request):
    return render(request, 'project/view-cv.html')