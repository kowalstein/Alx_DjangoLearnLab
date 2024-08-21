from django.contrib import admin
from .models import Book

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")

    search_fields = ("title", "author")

    list_filter = ("publication_year")
    
# Register your models here.
# advanced_features_and_security/users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm  # You'll need to create this form
    form = CustomUserChangeForm  # You'll need to create this form

    list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
