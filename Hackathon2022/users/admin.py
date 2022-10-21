from django.contrib.admin import ModelAdmin, register
from users.models import User


@register(User)
class AdminPanelUser(ModelAdmin):
    list_display = ('email', 'is_staff', 'is_superuser', 'date_joined', 'last_login',)
    list_filter = ('email', 'is_staff', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('is_superuser',)
