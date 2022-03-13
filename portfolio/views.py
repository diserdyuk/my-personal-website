from ssl import HAS_TLSv1_3
from django.shortcuts import render
from .models import Project


def home(request):
    # collect all data from db in var projects and send to template
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})



