from django.contrib import admin
from .models import Intern, User, Mentor
# Register your models here.
admin.site.register(User)
admin.site.register(Mentor)
admin.site.register(Intern)
