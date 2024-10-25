from django.contrib import admin

from .models import PersonalInformation, Contact, ProfessionalExperience, AcademicBackground

admin.site.register(PersonalInformation)
admin.site.register(Contact)
admin.site.register(ProfessionalExperience)
admin.site.register(AcademicBackground)
