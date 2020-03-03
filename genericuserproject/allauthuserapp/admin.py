from django.contrib import admin
from django.conf import settings
from allauthuserapp import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdminPanel(BaseUserAdmin):
    list_display = ('id', 'name', 'email', 'mobile_no', 'is_supervisor', 'is_gaurd', 'is_staff', 'is_superuser','is_active')
    # search_fields = ('emai','mobile_no','name','first_name','last_name',)
    # readonly_fields = ('date_joined','last_login',)
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('User Info', {'fields': ('name','first_name','last_name','mobile_no')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_supervisor','is_gaurd','is_superuser')}),
    )
    search_fields = ('email','first_name','last_name')
    # readonly_fields = ('date_joined','last_login')
    ordering = ('email','first_name','last_name')
    filter_horizontal = ()

admin.site.register(models.UserProfile, UserAdminPanel)
