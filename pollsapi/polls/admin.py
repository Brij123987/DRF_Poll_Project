from django.contrib import admin
from polls.models import Polls, Choice

# Register your models here.

admin.site.register(Polls)
admin.site.register(Choice)