from django.shortcuts import render, redirect
from .models import Applicant, ApplicantForm, SearchSkill, SKILLS

def index(request):
    if request.method == 'POST' :
        form = SearchSkill(request.POST)
        skillsList = request.POST.getlist('skills')
        applicants = Applicant.objects.all()
        filtered_applicants = []
        for applicant in  applicants :
            if all(x in applicant.skills for x in skillsList) :
                filtered_applicants.append(applicant)
        applicants = filtered_applicants
                    
    else :
        form = SearchSkill()
        applicants = Applicant.objects.all()


    context={'applicants': applicants, 'form': form, 'SKILLS': SKILLS}
    return render(request, 'cv/index.html', context)

def upload(request):
    if request.method == 'POST' :
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            form.full_clean()
            return redirect('cvUploaded')
    else :
        form =ApplicantForm()
    context = {'applicant_form': form}
    return render(request, 'cv/upload.html', context)

def uploaded(request) :
    return render(request, 'cv/uploaded.html')