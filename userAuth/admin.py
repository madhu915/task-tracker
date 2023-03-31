from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Comment, Intern, Task, User, Mentor
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Mentor)
admin.site.register(Intern)
admin.site.register(Task)
admin.site.register(Comment)