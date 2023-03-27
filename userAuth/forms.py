from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Intern, Task, User
class SignUpForm(UserCreationForm):
    role = forms.CharField(max_length=100, help_text='Required. Specify role (mentor/intern).')
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('role',)

class NewTaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.TextInput(attrs={'min': date.today(), 'value': date.today(), 'type': 'date', 'class':'date-input'}))

    class Meta:
        model = Task
        fields = ('internid', 'description','due_date', 'progress_status')
    # def __init__(self, *args, **kwargs):
    #     self.internid_id = forms.ModelChoiceField(label='Select Intern', queryset=Intern.objects.filter(mentorid_id=kwargs.pop('user', None)),
    #                            empty_label='--Select Intern--')    
    # def __init__(self, *args, **kwargs):
    #     user_id = kwargs.pop('user_id', None)
    #     super(NewTaskForm, self).__init__(*args, **kwargs)
    #     self.fields['internid'] = forms.ModelChoiceField(queryset=Intern.objects.filter(mentorid_id=user_id).values(),
    #                            empty_label='--Select Intern--') 
        # if user_id is not None:
        #     self.fields['internid'].queryset = Intern.objects.filter(mentorid_id=5)
        # else:
        #     self.fields['internid'].queryset = Intern.objects.none()    
