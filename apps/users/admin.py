from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from django.contrib.auth.admin import UserAdmin
from django import forms

# Custom form to remove password field from the admin add user form
class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)  # Only email is required

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password("default@123")  # Set a default password
        if commit:
            user.save()
        return user

class UserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm  # Use the custom form
    list_display = ('id','email','first_name', 'last_name','phone_number', 'is_staff', 'is_active','gender','is_company_owner','created','modified')
    list_filter = ('is_staff', 'is_active')
    readonly_fields = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth','phone_number','postal_code','address','city','country','gender')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_company_owner','groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email',  'is_staff','is_active','is_company_owner','date_of_birth','phone_number','address','city','country','gender','postal_code','groups', 'user_permissions')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    def get_form(self, request, obj=None, **kwargs):
        """
        Override the form to remove the password field when creating a user.
        """
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # If adding a new user
            form.base_fields.pop("password1", None)
            form.base_fields.pop("password2", None)
        return form

admin.site.register(User, UserAdmin)