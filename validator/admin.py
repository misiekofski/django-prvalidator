from django.contrib import admin
from .models import PR, Repository

# Register your models here.
admin.site.register(PR)
admin.site.register(Repository)