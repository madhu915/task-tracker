from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Task, User
class SignUpForm(UserCreationForm):
    role = forms.CharField(max_length=100, help_text='Required. Specify role (mentor/intern).')
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('role',)

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('internid', 'description','due_date', 'progress_status')
