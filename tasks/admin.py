from django.contrib import admin
from tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status',)
    search_fields = ('title', 'status',)
    list_filter = ('status',)
