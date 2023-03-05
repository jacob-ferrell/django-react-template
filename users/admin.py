from django.contrib import admin
from .models import NewUser

class NewUserAdmin(admin.ModelAdmin):
    list_display=('email', 'username', 'first_name', 'is_staff')

admin.site.register(NewUser, NewUserAdmin)