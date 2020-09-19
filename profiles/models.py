from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile", limit_choices_to={'user_type': 'S'})
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_profile", limit_choices_to={'user_type': 'T'})
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)


    def __str__(self):
        return self.first_name + ' ' + self.last_name



class OrganizationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization_profile', limit_choices_to={'user_type': 'O'})
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

