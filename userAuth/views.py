from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewTaskForm, SignUpForm
from .models import Intern, Task

def home(request):
    content = {}
    if request.user.is_authenticated:
        if request.user.role == 'Mentor':
            pending_tasks = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='To-Do')
            in_progress_tasks = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='In-Progress')
            completed_tasks = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='Completed')
        else:
            pending_tasks = Task.objects.filter(internid_id=request.user.id,progress_status__iexact='To-Do')
            in_progress_tasks = Task.objects.filter(internid_id=request.user.id,progress_status__iexact='In-Progress')
            completed_tasks = Task.objects.filter(internid_id=request.user.id,progress_status__iexact='Completed')
        content = {'to_do':pending_tasks,'in_progress':in_progress_tasks,'completed':completed_tasks}
    return render(request, 'auth/widgets/main.html',content)

def intern_details(request):
    usee=request.user.id
    interns_list=Intern.objects.filter(mentorid_id=usee)
    return render(request, 'auth/widgets/tables.html',{'intern_obj':interns_list})

def new_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.mentor_id=request.user.id
            task.last_updated_by_id=request.user.id
            task.save()

        return redirect('home')
    else:
        form = NewTaskForm()
        return render(request, 'auth/widgets/new_task.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', { 'form' : form })