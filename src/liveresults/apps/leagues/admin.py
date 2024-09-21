from django.contrib import admin

from .models import League

# Register your models here.


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'country','continent' ,'is_active')
    list_filter = ('is_active', 'created_at', 'updated_at',
                   'country', 'continent')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug':('name',)}