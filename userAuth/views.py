from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core import serializers
from .forms import NewTaskForm, SignUpForm
from .models import Intern, Task

def home(request):
    content = {}
    if request.user.is_authenticated:
        if request.user.role == 'Mentor':
            pending_tasks = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='To-Do')
            in_progress_tasks = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='In-Progress')
            completed_tasks = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='Completed')
            interns_list=Intern.objects.filter(mentorid_id=request.user.id)
        else:
            pending_tasks = Task.objects.filter(internid_id=request.user.id,progress_status__iexact='To-Do')
            in_progress_tasks = Task.objects.filter(internid_id=request.user.id,progress_status__iexact='In-Progress')
            completed_tasks = Task.objects.filter(internid_id=request.user.id,progress_status__iexact='Completed')
        content = {'to_do':pending_tasks,'in_progress':in_progress_tasks,'completed':completed_tasks,'interns':interns_list}
    return render(request, 'auth/widgets/main.html',content)


def name_api(request):
    id = request.GET.get('id')
    intern = Intern.objects.get(internid_id=id)
    data = {
        'name': f'{intern.firstname} {intern.lastname}'
    }
    return JsonResponse(data)

def intern_details(request):
    usee=request.user.id
    interns_list=Intern.objects.filter(mentorid_id=usee)
    return render(request, 'auth/widgets/tables.html',{'intern_obj':interns_list})

def new_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST,user=request.user.id)
        if form.is_valid():
            task=form.save(commit=False)
            task.internid_id=form.cleaned_data.get('intern')
            task.mentor_id=request.user.id
            task.last_updated_by_id=request.user.id
            task.save()
        else:
            print("Invalid Form")
            print(form.errors)

        return redirect('home')
    else:
        form=NewTaskForm(user=request.user.id)
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