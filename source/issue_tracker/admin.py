from django.contrib import admin

from issue_tracker.models import Task
from issue_tracker.models import Status
from issue_tracker.models import Type

from issue_tracker.models import Project


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'summary',
        'description',
        'created_at',
        'updated_at',
        'is_deleted',
        'deleted_at'
    )
    list_editable = ('summary', 'description', 'is_deleted')


admin.site.register(Task, TaskAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']


admin.site.register(Status, StatusAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']


admin.site.register(Type, TypeAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'completed_at', 'is_deleted', 'deleted_at')
    list_editable = ['name', 'created_at', 'completed_at', 'is_deleted', ]


admin.site.register(Project, ProjectAdmin)
