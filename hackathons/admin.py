from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Hackathon)
admin.site.register(models.HackathonRegistration)
admin.site.register(models.Submission)
