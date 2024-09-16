from django.contrib import admin

from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin', 'created_at', 'updated_at')
    list_filter = ('is_admin', 'created_at', 'updated_at')
    list_editable = ('is_admin',)