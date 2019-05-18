from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

ITEM_STATUSES = (
    ('A', 'Active'),
    ('D', 'Deleted'),
    ('N', 'Not active'),
    ('M', 'Merged to master'),
    ('T', 'Test')
)

class StoryQuerySet(models.QuerySet):
    def current_user_repos(self, user):
        return self.filter(
            Q(owner=user)
        )


class ProjectQuerySet(models.QuerySet):
    def current_user_prs(self, user):
        return self.filter(
            Q(owner=user)
        )


# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(User, related_name="project_owner", on_delete=models.PROTECT)
    name = models.CharField(max_length=100, default="New Project")
    description = models.CharField(max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='N', choices=ITEM_STATUSES)

    objects = ProjectQuerySet.as_manager()


class Story(models.Model):
    creator = models.ForeignKey(User, related_name="story_creator", on_delete=models.PROTECT)
    assigned_to = models.ForeignKey(User, related_name="assigned_story_user", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default="New Story")
    description = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=1, default='N', choices=ITEM_STATUSES)
    project = models.ForeignKey(Project, related_name="project", on_delete=models.CASCADE)

    objects = StoryQuerySet.as_manager()

class Task(models.Model):
    creator = models.ForeignKey(User, related_name="task_creator", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, related_name="assigned_task_user", on_delete=models.PROTECT)
    name = models.CharField(max_length=100, default="Unnamed PR")
    description = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=1, default='N', choices=ITEM_STATUSES)
    story = models.ForeignKey(Story, related_name="story", on_delete=models.CASCADE)

    objects = StoryQuerySet.as_manager()
