from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('personalInformation/', views.personalInformation_manager, name='personalInformation_manager'),
    path('personalInformation/<int:requestedId>', views.personalInformation_manager, name='personalInformation_manager_parameter'),
]