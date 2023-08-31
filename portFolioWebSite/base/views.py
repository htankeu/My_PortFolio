from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Project, Skill, SprachSkills, Message
from .form import ProjectForm, MessageForm

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    sprachSkills = SprachSkills.objects.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message is successfully sent')

    context = {'projects': projects, 'skills': skills, 'sprachSkills': sprachSkills, 'messageForm': form}
    return render(request, 'base/index.html', context)

def projectPage(request, pk):
    project = Project.objects.get(id=pk)

    return render(request, 'base/project.html', {'project': project})

def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/project_form.html', {'form': form})


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/project_form.html', {'form': form})


def inboxPage(request):
    message = Message.objects.all().order_by('is_read')
    unreadCount = Message.objects.filter(is_read=False).count()

    context = {'inbox': message, 'unreadcount': unreadCount}
    return render(request, 'base/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    return render(request, 'base/message.html', {'message': message})