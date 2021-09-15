from django.contrib import admin
from .models import User, Agent


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_agent', 'is_superuser']


admin.site.register(User, UserAdmin)
admin.site.register(Agent)
