from django.contrib import admin

# Register your models here.
from screenshots.models import Website
admin.site.register(Website)
from django.contrib.auth.models import Group

admin.site.unregister(Group)
from django.contrib.auth.models import User
admin.site.unregister(User)
