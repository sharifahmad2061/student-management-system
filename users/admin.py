from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, StudentProfile
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_student', 'is_staff', 'is_admin']
    list_filter = ['is_student', 'is_admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_student', 'is_staff', 'is_admin')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        })
    )
    search_fields = ['email', ]
    ordering = ['email', ]
    filter_horizontal = ()


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    pass
