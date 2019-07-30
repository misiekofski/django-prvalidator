from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from projects.views import ProjectsView, StoriesView, TasksView, ProjectDetailView, StoryDetailView, HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('projects/', ProjectsView.as_view(), name='project_list'),
    path('projects/<int:id>', ProjectDetailView.as_view(), name='project_details'),
    path('stories/', StoriesView.as_view(), name='stories_list'),
    path('stories/<int:id>', StoryDetailView.as_view(), name='story_details'),
    path('tasks/', TasksView.as_view(), name='task_list'),
    path('login/', LoginView.as_view(template_name='projects/login_form.html'), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
]