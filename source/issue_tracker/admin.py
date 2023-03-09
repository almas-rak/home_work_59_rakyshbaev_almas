from django.contrib import admin

from issue_tracker.models import Task
from issue_tracker.models import Status
from issue_tracker.models import Type


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'summary',
        'description',
        'status',
        'type',
        'created_at',
        'updated_at',
        'is_deleted',
        'deleted_at'
    )
    list_editable = ('summary', 'description', 'status', 'type', 'is_deleted')


admin.site.register(Task, TaskAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']


admin.site.register(Status, StatusAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']


admin.site.register(Type, TypeAdmin)
