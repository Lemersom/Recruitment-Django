from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import PersonalInformation
# , Contact, ProfessionalExperience, AcademicBackground
from .serializers import PersonalInformationSerializer
# , ContactSerializer, ProfessionalExperienceSerializer, AcademicBackgroundSerializer

import json


@api_view(['GET','POST','PUT','DELETE'])
def personalInformation_manager(request, requestedId=None):

    # GET_ALL
    if request.method == 'GET' and requestedId is None:
        personalInformationList = PersonalInformation.objects.all()
        serializer = PersonalInformationSerializer(personalInformationList, many=True)

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
        toCreate_personalInformation = request.data

        serializer = PersonalInformationSerializer(data=toCreate_personalInformation)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE
    if request.method == 'PUT' and requestedId:
        try:
            toUpdate_personalInformation = PersonalInformation.objects.get(pk=requestedId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonalInformationSerializer(toUpdate_personalInformation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    if request.method == 'DELETE' and requestedId:
        try:
            toDelete_personalInformation = PersonalInformation.objects.get(pk=requestedId)
            toDelete_personalInformation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

    return Response(status=status.HTTP_400_BAD_REQUEST)
