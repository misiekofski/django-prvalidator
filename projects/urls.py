from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.validator_index, name='index'),
    path('projects/', views.all_projects, name='project_list'),
    path('projects/<int:id>', views.project_details, name='project_details'),
    path('stories/', views.all_stories, name='stories_list'),
    path('stories/<int:id>', views.story_details, name='story_details'),
    path('tasks/', views.all_tasks, name='task_list'),
    path('login/', LoginView.as_view(template_name='projects/login_form.html'), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
]