from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CostumUserCreationForm, CostumUserChangeForm
from .models import CostumUser

# Register your models here.

class CostumUserAdmin(UserAdmin):
    add_form=CostumUserCreationForm
    form=CostumUserChangeForm
    model=CostumUser
    list_display = ['email','username','age','is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields': ('age',),}),
    )
    add_fieldsets=UserAdmin.add_fieldsets + (
        (None,{'fields':('age',)}),
    )

admin.site.register(CostumUser, CostumUserAdmin)
