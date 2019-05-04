from django.shortcuts import render
from django.http import HttpResponse
from .models import PR, Repository


# Create your views here.
def validator_index(request):
    return HttpResponse("Validator is UP.")


def pr_details(request, id):
    details = PR.objects.get(pk=id);
    return HttpResponse("Pr name: " + details.name + "<br>" +
                        "Status: " + details.status + "<br>" +
                        "Created by: " + str(details.created) + "<br>" +
                        "Owner: " + str(details.owner) + "<br>" +
                        "Description: " + details.description + "<br>" +
                        "Already merged: " + str(details.merged) + "<br>")


def repo_details(request, id):
    details = Repository.objects.get(pk=id);
    return HttpResponse("Pr name: " + details.name + "<br>" +
                        "Status: " + details.status + "<br>" +
                        "Created by: " + str(details.created) + "<br>" +
                        "Owner: " + str(details.owner) + "<br>" +
                        "Description: " + details.description + "<br>")


def all_prs(request):
    allprs = PR.objects.all()
    prlist = ''
    for pr in allprs:
        prlist += pr.name + "<br>"
    return HttpResponse("All PR details: <br>" + prlist)


def all_repos(request):
    allrepos = Repository.objects.all()
    repolist = ''
    for repo in allrepos:
        repolist += repo.name + "<br>"
    return HttpResponse("All PR details: <br>" + repolist)
