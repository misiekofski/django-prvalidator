from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.validator_index, name='index'),
    path('project/', views.all_projects, name='project_list'),
    path('project/<int:id>', views.project_details, name='project_details'),
    path('story/', views.all_stories, name='stories_list'),
    path('story/<int:id>', views.story_details, name='story_details'),
    path('login/', LoginView.as_view(template_name='validator/login_form.html'), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
]