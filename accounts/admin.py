from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User

admin.site.unregister(Group)

class UserModelAdmin(admin.ModelAdmin):
    """
        User for overriding the normal user admin panel, and add the extra fields added to the user
    """

    def save_model(self, request, obj, form, change):
        # Override this to set the password to the value in the field if it's
        # changed.
        if User.objects.filter(pk=obj.pk).exists():
            orig_obj = User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()


admin.site.register(User, UserModelAdmin)