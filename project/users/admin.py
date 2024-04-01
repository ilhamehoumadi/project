from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
 
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    # Define the form to use for adding and changing users
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

    

# Register the CustomUserAdmin with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
