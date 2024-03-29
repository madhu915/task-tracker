from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from userAuth import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'),name='login'),
    re_path(r'^.*logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name="signup"),
    path('interns/',views.intern_details,name='interns'),
    path('new-task/', views.new_task, name='new_task'),
    path('get-name/',views.name_api,name='get_name'),
    path('intern-filter/',views.intern_filter,name='intern-filter'),
    path('reset-password/',views.reset,name='reset'),
    path('reset/',views.new_password,name='new-password'),
    path('task/<int:pk>/',views.task_details,name='task-detail'),
    path('user-profile/',views.my_profile,name='profile'),
    path('update/',views.update,name='update'),
    path('update-tasks/',views.update_tasks,name='update-tasks'),
    path('new-comment/',views.new_comment,name='new-comment'),
    path('upload-file/',views.upload_file,name='upload-file'),
    path('add-tasks/',views.add_tasks,name='add-tasks'),
]