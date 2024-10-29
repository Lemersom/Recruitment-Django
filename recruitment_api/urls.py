from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('profile/', views.completeProfile_manager, name='completeProfile_manager'),
    path('information/', views.personalInformation_manager, name='personalInformation_manager'),
    path('information/<int:requestedId>', views.personalInformation_manager, name='personalInformation_manager_parameter'),
    path('contact/', views.contact_manager, name='contact_manager'),
    path('contact/<int:requestedId>', views.contact_manager, name='contact_manager_parameter'),
    path('experience/', views.professionalExperience_manager, name='professionalExperience_manager'),
    path('experience/<int:requestedId>', views.professionalExperience_manager, name='professionalExperience_manager_parameter'),
    path('academic/', views.academicBackground_manager, name='academicBackground_manager'),
    path('academic/<int:requestedId>', views.academicBackground_manager, name='academicBackground_manager_parameter'),
]