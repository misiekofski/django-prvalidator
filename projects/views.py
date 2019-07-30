from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView

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

    def post(self, request):
        form = StoryForm(request.POST)
        if form.is_valid():
            creator = form.cleaned_data['creator']
            assigned_to = form.cleaned_data['assigned_to']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            project = form.cleaned_data['project']
            Story.objects.create(creator=creator, assigned_to=assigned_to, name=name, description=description, status=status, project=project)
            return HttpResponseRedirect(reverse('stories_list'))


class ProjectsView(LoginRequiredMixin, View):
    def get(self, request):
        my_projects = Project.objects.current_user_projects(request.user)
        form = ProjectForm()
        return render(request, 'projects/projects.html',
                      {'num_projects': Project.objects.count(),
                       'my_projects': my_projects,
                       'form': form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            owner = form.cleaned_data['owner']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            Project.objects.create(owner=owner, name=name, description=description, status=status)
            return HttpResponseRedirect(reverse('project_list'))


class TasksView(LoginRequiredMixin, View):
    def get(self, request):
        my_tasks = Task.objects.current_user_tasks(request.user)
        form = TaskForm()
        return render(request, 'projects/tasks.html',
                      {'num_tasks': Task.objects.count(),
                       'my_tasks': my_tasks,
                       'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            creator = form.cleaned_data['creator']
            assigned_to = form.cleaned_data['assigned_to']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            story = form.cleaned_data['story']
            Task.objects.create(creator=creator, assigned_to=assigned_to, name=name, description=description, status=status, story=story)
            return HttpResponseRedirect(reverse('task_list'))
