from django.shortcuts import render
from django.http import HttpResponse
from .models import PR, Repository


# Create your views here.
def validator_index(request):
    return render(request, 'welcome.html')


def pr_details(request, id):
    details = PR.objects.get(pk=id)
    return render(request, 'validator/pr_details.html')
    # return HttpResponse("Pr name: " + details.name + "<br>" +
    #                    "Status: " + details.status + "<br>" +
    #                    "Created by: " + str(details.created) + "<br>" +
    #                    "Owner: " + str(details.owner) + "<br>" +
    #                    "Description: " + details.description + "<br>" +
    #                    "Already merged: " + str(details.merged) + "<br>")


def repo_details(request, id):
    details = Repository.objects.get(pk=id)
    return render(request, 'validator/repo_details.html')


def all_prs(request):
    myprs = PR.objects.current_user_prs(request.user)
    return render(request, 'validator/prs.html',
                  {'nprs': PR.objects.count(),
                   'allprs': myprs})


def all_repos(request):
    myrepos = Repository.objects.current_user_repos(request.user)
    return render(request, 'validator/repos.html',
                  {'nrepos': Repository.objects.count(),
                   'allrepos': myrepos})
