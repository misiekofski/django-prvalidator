from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PR, Repository


# Create your views here.
def validator_index(request):
    if request.user.is_authenticated:
        return redirect('repo_list')
    else:
        return render(request, 'welcome.html')


@login_required
def pr_details(request, id):
    details = PR.objects.get(pk=id)
    return render(request, 'validator/pr_details.html')
    # return HttpResponse("Pr name: " + details.name + "<br>" +
    #                    "Status: " + details.status + "<br>" +
    #                    "Created by: " + str(details.created) + "<br>" +
    #                    "Owner: " + str(details.owner) + "<br>" +
    #                    "Description: " + details.description + "<br>" +
    #                    "Already merged: " + str(details.merged) + "<br>")


@login_required
def repo_details(request, id):
    details = Repository.objects.get(pk=id)
    return render(request, 'validator/repo_details.html')


@login_required
def all_prs(request):
    myprs = PR.objects.current_user_prs(request.user)
    return render(request, 'validator/prs.html',
                  {'nprs': PR.objects.count(),
                   'allprs': myprs})


@login_required
def all_repos(request):
    myrepos = Repository.objects.current_user_repos(request.user)
    return render(request, 'validator/repos.html',
                  {'nrepos': Repository.objects.count(),
                   'allrepos': myrepos})
