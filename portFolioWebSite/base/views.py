from django.shortcuts import render
from .models import Project

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    return render(request,'base/index.html',{'projects':projects})