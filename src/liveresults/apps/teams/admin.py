from django.contrib import admin

from .models import Team, Honor

# Register your models here.

class HonorAdminInLine(admin.StackedInline):
    model = Honor


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'league_name')
    list_filter = ('city', 'established_date')
    prepopulated_fields = {'slug': ('name',)}

    inlines = [HonorAdminInLine]
