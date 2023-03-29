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
        user_id=kwargs.pop('user')
        super(NewTaskForm, self).__init__(*args, **kwargs)
        if user_id:
            self.fields['intern'] = forms.ModelChoiceField(queryset=Intern.objects.filter(mentorid_id=user_id).values_list(flat=True), 
                empty_label='-- Select Intern ID --')
            
    due_date = forms.DateField(widget=forms.TextInput(attrs={'min': date.today(), 'value': date.today(), 'type': 'date', 'class':'date-input'}))
    progress_status = forms.CharField(widget=forms.Select(choices=[('To-do','To-Do'),('In-Progress','In-Progress'),('completed','Completed')]))
    intern = forms.ModelChoiceField(queryset=Intern.objects.all(),empty_label='-- Select Intern ID --')
    intern_name= forms.CharField(disabled=True)
    class Meta:
        model = Task
        fields = ('intern','intern_name','description','due_date', 'progress_status') 
