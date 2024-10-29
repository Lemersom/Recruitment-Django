from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import transaction

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import PersonalInformation, Contact, ProfessionalExperience, AcademicBackground
from .serializers import PersonalInformationSerializer, ContactSerializer, ProfessionalExperienceSerializer, AcademicBackgroundSerializer

import json


### Complete Profile ###
@api_view(['POST'])
def completeProfile_manager(request):
    try:
        with transaction.atomic():
            # Personal Information
            personal_serializer = PersonalInformationSerializer(data=request.data.get('personal_information'))
            if personal_serializer.is_valid(raise_exception=True):
                personal_info_instance = personal_serializer.save()

            # Contact
            contact_data = request.data.get('contact', {})
            contact_data['personal_information'] = personal_info_instance.id
            contact_serializer = ContactSerializer(data=contact_data)
            if contact_serializer.is_valid(raise_exception=True):
                contact_serializer.save()

            # Professional Experience
            experience_data = request.data.get('professional_experience', {})
            experience_data['personal_information'] = personal_info_instance.id
            experience_serializer = ProfessionalExperienceSerializer(data=experience_data)
            if experience_serializer.is_valid(raise_exception=True):
                experience_serializer.save()

            # Academic Background
            academic_data = request.data.get('academic_background', {})
            academic_data['personal_information'] = personal_info_instance.id
            academic_serializer = AcademicBackgroundSerializer(data=academic_data)
            if academic_serializer.is_valid(raise_exception=True):
                academic_serializer.save()

        return Response({"message": "Profile created successfully."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


### Personal Information ###
@api_view(['GET','POST','PUT','DELETE'])
def personalInformation_manager(request, requestedId=None):

    # GET_ALL
    if request.method == 'GET' and requestedId is None:
        personalInformation_list = PersonalInformation.objects.all()
        serializer = PersonalInformationSerializer(personalInformation_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # GET_BY_ID
    if request.method == 'GET' and requestedId:
        try:
            personalInformation = PersonalInformation.objects.get(pk=requestedId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonalInformationSerializer(personalInformation)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # CREATE
    if request.method == 'POST':
        serializer = PersonalInformationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE
    if request.method == 'PUT' and requestedId:
        try:
            personalInformation_toUpdate = PersonalInformation.objects.get(pk=requestedId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonalInformationSerializer(personalInformation_toUpdate, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    if request.method == 'DELETE' and requestedId:
        try:
            personalInformation_toDelete = PersonalInformation.objects.get(pk=requestedId)
            personalInformation_toDelete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Invalid request method
    return Response(status=status.HTTP_400_BAD_REQUEST)


### Contact ###
@api_view(['GET','POST','PUT','DELETE'])
def contact_manager(request, requestedId=None):

    # GET_ALL
    if request.method == 'GET' and requestedId is None:
        contact_list = Contact.objects.all()
        serializer = ContactSerializer(contact_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # GET_BY_ID
    if request.method == 'GET' and requestedId:
        try:
            contact = Contact.objects.get(pk=requestedId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ContactSerializer(contact)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # CREATE
    if request.method == 'POST':
        contact_toCreate = request.data

        serializer = ContactSerializer(data=contact_toCreate)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE
    if request.method == 'PUT' and requestedId:
        try:
            contact_toUpdate = Contact.objects.get(pk=requestedId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ContactSerializer(contact_toUpdate, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    if request.method == 'DELETE' and requestedId:
        try:
            contact_toDelete = Contact.objects.get(pk=requestedId)
            contact_toDelete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Invalid request method
    return Response(status=status.HTTP_400_BAD_REQUEST)


### Professional Experience ###
@api_view(['GET','POST','PUT','DELETE'])
def professionalExperience_manager(request, requestedId=None):

    # GET_ALL
    if request.method == 'GET' and requestedId is None:
        experience_list = ProfessionalExperience.objects.all()
        serializer = ProfessionalExperienceSerializer(experience_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # GET_BY_ID
    if request.method == 'GET' and requestedId:
        try:
            experience = ProfessionalExperience.objects.get(pk=requestedId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfessionalExperienceSerializer(experience)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # CREATE
    if request.method == 'POST':
        experience_toCreate = request.data

        serializer = ProfessionalExperienceSerializer(data=experience_toCreate)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE
    if request.method == 'PUT' and requestedId:
        try:
            experience_toUpdate = ProfessionalExperience.objects.get(pk=requestedId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfessionalExperienceSerializer(experience_toUpdate, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    if request.method == 'DELETE' and requestedId:
        try:
            experience_toDelete = ProfessionalExperience.objects.get(pk=requestedId)
            experience_toDelete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Invalid request method
    return Response(status=status.HTTP_400_BAD_REQUEST)


### Academic Background ###
@api_view(['GET','POST','PUT','DELETE'])
def academicBackground_manager(request, requestedId=None):

    # GET_ALL
    if request.method == 'GET' and requestedId is None:
        education_list = AcademicBackground.objects.all()
        serializer = AcademicBackgroundSerializer(education_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # GET_BY_ID
    if request.method == 'GET' and requestedId:
        try:
            education = AcademicBackground.objects.get(pk=requestedId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AcademicBackgroundSerializer(education)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # CREATE
    if request.method == 'POST':
        education_toCreate = request.data

        serializer = AcademicBackgroundSerializer(data=education_toCreate)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE
    if request.method == 'PUT' and requestedId:
        try:
            education_toUpdate = AcademicBackground.objects.get(pk=requestedId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AcademicBackgroundSerializer(education_toUpdate, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    if request.method == 'DELETE' and requestedId:
        try:
            education_toDelete = AcademicBackground.objects.get(pk=requestedId)
            education_toDelete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Invalid request method
    return Response(status=status.HTTP_400_BAD_REQUEST)
