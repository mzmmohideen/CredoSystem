from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import PrivilegeClass, PrivilegeClassGroup
# Register your models here.


@admin.register(get_user_model())
class MyUserAdmin(admin.UserAdmin):
    readonly_fields = ('groups', )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',), 'fields': ('username', 'first_name', 'last_name', 'email',
                                                 'password1', 'password2')
            }
        ),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'priv_class_id')



class SampleTabular(admin.TabularInline):
    model = PrivilegeClassGroup


@admin.register(PrivilegeClass)
class PrivilegeClassAdmin(admin.ModelAdmin):
    inlines = [
        SampleTabular,
    ]



@admin.register(PrivilegeClassGroup)
class PrivilegeClassGroupAdmin(admin.ModelAdmin):
	pass
# admin.site.register(PrivilegeClass, PrivilegeClassAdmin)
# admin.site.register(PrivilegeClassGroup)
