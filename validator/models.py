from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Repository(models.Model):
    owner = models.ForeignKey(User, related_name="repo_owner", on_delete=models.PROTECT)
    name = models.CharField(max_length=100, default="Unnamed Repository")
    description = models.CharField(max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='N')

    def __str__(self):
        return "Repository {0}, owned by: {1}".format(
            self.name, self.owner
        )


class PR(models.Model):
    owner = models.ForeignKey(User, related_name="pr_creator", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default="Unnamed PR")
    description = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=1, default='N')
    merged = models.BooleanField()
    repo = models.ForeignKey(Repository, related_name="repository", on_delete=models.CASCADE)

    def __str__(self):
        return "PR {0}, created by: {1}".format(
            self.name, self.owner
        )
