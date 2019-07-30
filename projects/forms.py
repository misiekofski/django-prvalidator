from django.forms import ModelForm

from .models import Project, Story, Task


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['owner', 'name', 'description', 'status']


class StoryForm(ModelForm):
    class Meta:
        model = Story
        exclude = ['created']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['created']
