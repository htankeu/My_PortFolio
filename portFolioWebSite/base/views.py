from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Project, Skill, SprachSkills, Message, Endorsement
from .form import ProjectForm, MessageForm, SkillForm, EndorsementForm, commentForm

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    sprachSkills = SprachSkills.objects.all()
    endorsements = Endorsement.objects.filter(approved=True)
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message is successfully sent')

    context = {'projects': projects, 'skills': skills, 'sprachSkills': sprachSkills, 'messageForm': form, 'endorsements':endorsements}
    return render(request, 'base/index.html', context)

def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    count = project.comment_set.count()
    comments = project.comment_set.all().order_by('-created')
    form = commentForm()

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(request, "Thanks for Comment!")
            redirect('project')

    context = {'project': project, 'count': count, 'comments': comments, 'form': form}

    return render(request, 'base/project.html', context)

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

def addSkill(request):
    form = SkillForm()
    if(request.method == 'POST'):
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The Skill is added")
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/skill_form.html', context)

def addEndorsements(request):
    form = EndorsementForm()
    if(request.method == 'POST'):
        form = EndorsementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you, your endorsement was successfully added!")
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/endorsement_form.html', context)