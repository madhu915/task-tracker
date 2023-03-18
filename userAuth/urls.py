from django.contrib.auth import views as auth_views
from django.urls import path
from userAuth import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name="signup"),
    path('interns/',views.intern_details,name='interns'),
]