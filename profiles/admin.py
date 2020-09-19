from django.contrib import admin

from .models import StaffProfile, StudentProfile, OrganizationProfile

admin.site.register(StaffProfile)
admin.site.register(StudentProfile)
admin.site.register(OrganizationProfile)