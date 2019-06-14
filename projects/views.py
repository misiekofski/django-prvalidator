from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Project, Story, Task


# Create your views here.
def validator_index(request):
    if request.user.is_authenticated:
        return redirect('project_list')
    else:
        return render(request, 'welcome.html')


@login_required
def story_details(request, id):
    details = Story.objects.get(pk=id)
    return render(request, 'projects/story_details.html',
                  {'details': details})

@login_required
def project_details(request, id):
    details = Project.objects.get(pk=id)
    return render(request, 'projects/project_details.html',
                  {'details': details})


@login_required
def all_stories(request):
    my_stories = Story.objects.current_user_stories(request.user)
    return render(request, 'projects/stories.html',
                  {'num_stories': Story.objects.count(),
                   'my_stories': my_stories})


@login_required
def all_projects(request):
    my_projects = Project.objects.current_user_projects(request.user)
    return render(request, 'projects/projects.html',
                  {'num_projects': Project.objects.count(),
                   'my_projects': my_projects})

@login_required
def all_tasks(request):
    my_tasks = Task.objects.current_user_tasks(request.user)
    return render(request, 'projects/tasks.html',
                  {'num_tasks': Task.objects.count(),
                   'my_tasks': my_tasks})