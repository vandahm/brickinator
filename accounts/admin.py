from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'email')
    search_fields = ['last_name', 'first_name', 'email', 'username']
    ordering = ['last_name', 'first_name']

    fieldsets = (
        ('Basic Information', {
            'fields': ('last_name', 'first_name', 'email'),
        }),

        ('Account Information', {
            'fields': ('username',),
        }),

        ('Advanced', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')
        })
    )