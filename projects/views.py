from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from projects.forms import ProjectForm, StoryForm, TaskForm
from .models import Project, Story, Task


# Create your views here.
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('project_list')
        else:
            return render(request, 'welcome.html')


class StoryDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        details = Story.objects.get(pk=id)
        tasks = Task.objects.filter(story=id)
        return render(request, 'projects/story_details.html',
                      {'details': details,
                       'tasks': tasks})


class ProjectDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        details = Project.objects.get(pk=id)
        stories = Story.objects.filter(project=id)
        return render(request, 'projects/project_details.html',
                      {'details': details,
                       'stories': stories})


class StoriesView(LoginRequiredMixin, View):
    def get(self, request):
        my_stories = Story.objects.current_user_stories(request.user)
        form = StoryForm()
        return render(request, 'projects/stories.html',
                      {'num_stories': Story.objects.count(),
                       'my_stories': my_stories,
                       'form': form})


class ProjectsView(LoginRequiredMixin, View):
    def get(self, request):
        my_projects = Project.objects.current_user_projects(request.user)
        form = ProjectForm()
        return render(request, 'projects/projects.html',
                      {'num_projects': Project.objects.count(),
                       'my_projects': my_projects,
                       'form': form})


class TasksView(LoginRequiredMixin, View):
    def get(self, request):
        my_tasks = Task.objects.current_user_tasks(request.user)
        form = TaskForm()
        return render(request, 'projects/tasks.html',
                      {'num_tasks': Task.objects.count(),
                       'my_tasks': my_tasks,
                       'form': form})