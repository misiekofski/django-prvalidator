from django.urls import path

from . import views

urlpatterns = [
    path('', views.validator_index, name='index'),
    path('pr/', views.all_prs, name='all pr list'),
    path('pr/<int:id>', views.pr_details, name='pr details'),
    path('repo/', views.all_repos, name='all repo list'),
    path('repo/<int:id>', views.repo_details, name='repo details'),
]