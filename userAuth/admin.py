from django.contrib import admin
from .models import Comment, Intern, Task, User, Mentor
# Register your models here.
admin.site.register(User)
admin.site.register(Mentor)
admin.site.register(Intern)
admin.site.register(Task)
admin.site.register(Comment)
