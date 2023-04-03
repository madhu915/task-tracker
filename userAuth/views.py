from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from .forms import NewTaskForm, SignUpForm
from .models import Comment, Intern, Mentor, Task, User

def home(request):
    content = {}
    if request.user.is_authenticated:
        interns_list=Intern.objects.filter(mentorid_id=request.user.id)
        if request.user.role == 'Mentor':
            pending = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='To-Do').order_by('-id')
            in_progress = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='In-Progress').order_by('-id')
            completed = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='Completed').order_by('-id')
        else:
            pending = Task.objects.filter(internid_id=request.user.id,progress_status__iexact='To-Do').order_by('-id')
            in_progress = Task.objects.filter(internid_id=request.user.id,progress_status__iexact='In-Progress').order_by('-id')
            completed = Task.objects.filter(internid_id=request.user.id,progress_status__iexact='Completed').order_by('-id')
        content = {'to_do':pending,'in_progress':in_progress,'completed':completed,'interns':interns_list}
    return render(request, 'auth/widgets/main.html',content)

def my_profile(request):
    if request.user.role == 'Mentor':
        user=Mentor.objects.get(mentorid_id=request.user.id)
    else:
        user=Intern.objects.get(internid_id=request.user.id)
    return render(request,'auth/widgets/profile.html',{'collab':user})

def task_details(request,pk):
    task=get_object_or_404(Task,id=pk)
    object=Comment.objects.filter(task_id=pk).exists()
    comment=Comment.objects.filter(task_id=pk) if object else None
    print(comment,object)
    context={'task':task,'comment':comment}
    return render(request, 'auth/widgets/task_details.html',context)
    
def reset(request):
    return render(request, 'auth/widgets/reset.html')

@csrf_exempt
def update(request):
    if request.user.role == 'intern':
        intern=get_object_or_404(Intern,pk=request.user.id)
        intern.email=request.POST.get('email')
        intern.firstname=request.POST.get('firstname')
        intern.lastname=request.POST.get('lastname')        
        intern.college=request.POST.get('college')
        intern.save()
    if request.user.role == 'Mentor':
        mentor=get_object_or_404(Mentor,pk=request.user.id)
        mentor.email=request.POST.get('email')
        mentor.firstname=request.POST.get('firstname')
        mentor.lastname=request.POST.get('lastname')
        mentor.save()
    return redirect('profile')

@csrf_exempt
def new_password(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        user.set_password(request.POST.get('password-verify'))
        user.save()
        print(request.POST.get('password-verify'),user.first_name)
    return redirect('home')

def name_api(request):
    id = request.GET.get('uuid')
    intern = Intern.objects.get(internid_id=id)
    data = {
        'name': f'{intern.firstname} {intern.lastname}'
    }
    return JsonResponse(data)

def intern_filter(request):
    to_do = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='To-Do').order_by('-id')
    in_progress = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='In-Progress').order_by('-id')
    completed = Task.objects.filter(mentor_id=request.user.id,progress_status__iexact='Completed').order_by('-id')

    interns_list=Intern.objects.filter(mentorid_id=request.user.id)
    category = request.GET.get('id')
    if category:
        to_do = to_do.filter(internid_id=category)
        in_progress = in_progress.filter(internid_id=category)
        completed = completed.filter(internid_id=category)
    content={'to_do': to_do,'in_progress': in_progress, 'completed': completed, 'interns':interns_list}
    return render(request, 'auth/widgets/main.html', content)

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