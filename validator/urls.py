from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.validator_index, name='index'),
    path('pr/', views.all_prs, name='pr_list'),
    path('pr/<int:id>', views.pr_details, name='pr_details'),
    path('repo/', views.all_repos, name='repo_list'),
    path('repo/<int:id>', views.repo_details, name='repo_details'),
    path('login/', LoginView.as_view(template_name='validator/login_form.html'), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
]