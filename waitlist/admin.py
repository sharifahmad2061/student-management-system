from django.contrib import admin
from .models import Waitlist
# Register your models here.


@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at')
    search_fields = ('first_name', 'last_name')
