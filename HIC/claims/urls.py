from django.urls import path
from . import views

urlpatterns = [
    path('claimdata/', views.getClaimData, name='allclaimdata'),
]
