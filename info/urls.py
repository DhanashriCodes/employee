from django.urls import path
from . import views

urlpatterns = [
    path('emp/',views.handleEmpRelationship),
    path('dept/', views.handleDept)
    
]