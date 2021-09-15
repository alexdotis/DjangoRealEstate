from django.contrib import admin
from .models import AssignmentProperty


class AssignmentPropertyAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'is_assigned']
    list_filter = ['status']


admin.site.register(AssignmentProperty, AssignmentPropertyAdmin)
