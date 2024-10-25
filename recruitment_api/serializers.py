from rest_framework import serializers

from .models import PersonalInformation
# , Contact, ProfessionalExperience, AcademicBackground


class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = '__all__'

# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = '__all__'

# class ProfessionalExperienceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProfessionalExperience
#         fields = '__all__'

# class AcademicBackgroundSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AcademicBackground
#         fields = '__all__'
