from django import forms
from django.core.exceptions import ValidationError

from issue_tracker.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Полное описание',
            'status': 'Статус',
            'type': 'Тип'
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 5:
            raise ValidationError('Краткое описание должно быть длинее 5 символов')
        return summary

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status:
            return status
        raise ValidationError('Статус задачи не выбран')

    def clean_type(self):
        type_task = self.cleaned_data.get('type')
        if type_task:
            return type_task
        raise ValidationError('Тип задачи не выбран')
