from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_queries/',views.all_model_queries, name='all_queries'),
    path('contact/', views.contactView, name='contact'),
    path('contactus/', views.ContactModelFormView, name='contactus'),
]