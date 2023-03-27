from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Intern, Task, User
class SignUpForm(UserCreationForm):
    role = forms.CharField(max_length=100, help_text='Field Required. Specify role (mentor/intern).')
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('role',)

class NewTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""
        user_id=kwargs.pop('user')
        super(NewTaskForm, self).__init__(*args, **kwargs)
        if user_id:
            self.fields['internid'] = forms.ModelChoiceField(queryset=Intern.objects.filter(mentorid_id=None) | Intern.objects.filter(
                mentorid_id=user_id).values(), empty_label='--Select Intern--')
            
    due_date = forms.DateField(widget=forms.TextInput(attrs={'min': date.today(), 'value': date.today(), 'type': 'date', 'class':'date-input'}))
    progress_status = forms.CharField(widget=forms.Select(choices=[('To-do','To-Do'),('In-Progress','In-Progress'),('completed','Completed')]))
    # internid = forms.ModelChoiceField(queryset=Intern.objects.all(),empty_label='--Select Intern--') 
    class Meta:
        model = Task
        fields = ('internid', 'description','due_date', 'progress_status') 
