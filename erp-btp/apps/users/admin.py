# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'company', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'company')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Informations professionnelles', {
            'fields': ('phone', 'company')
        }),
    )
    
    # SUPPRIMEZ la ligne ordering si elle existe
    # ordering = ('username',)  ← COMMENTEZ ou SUPPRIMEZ cette ligne