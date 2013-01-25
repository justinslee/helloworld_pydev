from hello_polls.models import MyPoll
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(MyPoll)
