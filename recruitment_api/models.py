from django.db import models

class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Contact(models.Model):
#     personal_information = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15)
#     country = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)

#     def __str__(self):
#         return f"Contact for {self.personal_information}"


# class ProfessionalExperience(models.Model):
#     personal_information = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, related_name='experiences')
#     job_title = models.CharField(max_length=100)
#     company = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField(blank=True, null=True)
#     description = models.TextField(default='')

#     def __str__(self):
#         return f"{self.job_title} at {self.company}"


# class AcademicBackground(models.Model):
#     personal_information = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, related_name='education')
#     institution = models.CharField(max_length=100)
#     degree = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.degree} from {self.institution}"
