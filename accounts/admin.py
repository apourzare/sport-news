from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('مشخصات فردی', {
            'fields': (('first_name', 'last_name'), 'phone')
        }),
        ('مشخصات کاربری', {
            'fields': (('username', 'password'),'email', ('is_active', 'is_staff', 'is_superuser'))
        }),

        ('اطلاعات ورود', {
            'classes': ('collapse','Amin'),
            'fields': (('user_permissions', 'groups'),('last_login', 'date_joined'))
        }),
    )
    readonly_fields = ('last_login', 'date_joined')
    

