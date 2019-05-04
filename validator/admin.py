from django.contrib import admin
from .models import PR, Repository

# Register your models here.
@admin.register(PR)
class PRAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'status', 'repo')
    list_editable = ('owner', 'status')

@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'status')
    list_editable = ('owner', 'status')