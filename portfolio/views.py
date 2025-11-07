
from django.shortcuts import render, redirect
from .models import Project, Contact

def home(request):
    return render(request, 'home.html')

def projects(request):
    data = Project.objects.all()
    return render(request, 'projects.html', {"projects": data})

def skills(request):
    return render(request, 'skills.html')

def experience(request):
    return render(request, 'experience.html')

def education(request):
    return render(request, 'education.html')

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        return redirect('contact')
    return render(request, 'contact.html')
