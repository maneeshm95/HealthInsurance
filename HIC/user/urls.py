from django.urls import path
from . import views

urlpatterns = [
    path('userregistration/', views.signup_view, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
