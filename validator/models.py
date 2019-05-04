from django.db import models
from django.contrib.auth.models import User

REPO_STATUSES = (
    ('A', 'Active'),
    ('D', 'Deleted'),
    ('N', 'Not active'),
    ('P', 'Production ready'),
    ('T', 'Test')
)

PR_STATUSES = (
    ('A', 'Active'),
    ('D', 'Deleted'),
    ('N', 'Not active'),
    ('M', 'Merged to master'),
    ('T', 'Test')
)

# Create your models here.
class Repository(models.Model):
    owner = models.ForeignKey(User, related_name="repo_owner", on_delete=models.PROTECT)
    name = models.CharField(max_length=100, default="Unnamed Repository")
    description = models.CharField(max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='N', choices=REPO_STATUSES)

class PR(models.Model):
    owner = models.ForeignKey(User, related_name="pr_creator", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default="Unnamed PR")
    description = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=1, default='N', choices=PR_STATUSES)
    merged = models.BooleanField()
    repo = models.ForeignKey(Repository, related_name="repository", on_delete=models.CASCADE)