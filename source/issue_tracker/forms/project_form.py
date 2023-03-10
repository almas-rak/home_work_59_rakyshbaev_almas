from django import forms

from issue_tracker.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('created_at', 'completed_at', 'name', 'description')
        labels = {
            'created_at': 'Дата создания',
            'completed_at': 'Дата окончания',
            'name': 'Название',
            'description': 'Описание',
        }
