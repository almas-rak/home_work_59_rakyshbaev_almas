# Generated by Django 4.1.7 on 2023-03-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0002_remove_task_project_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата и время удаления'),
        ),
        migrations.AddField(
            model_name='project',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AlterField(
            model_name='project',
            name='completed_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateField(verbose_name='Дата создания'),
        ),
    ]
