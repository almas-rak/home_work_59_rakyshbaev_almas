from django.db import models
from django.utils import timezone


class Task(models.Model):
    summary = models.CharField(
        max_length=100,
        verbose_name='Краткое описание'
    )

    description = models.TextField(
        null=True, blank=True,
        verbose_name='Полное описание'
    )

    status = models.ForeignKey(
        to='issue_tracker.Status',
        on_delete=models.RESTRICT,
        related_name='statuses',
        verbose_name='Статус'
    )

    type = models.ForeignKey(
        to='issue_tracker.Type',
        on_delete=models.RESTRICT,
        related_name='type',
        verbose_name='Тип'
    )

    is_deleted = models.BooleanField(
        default=False,
        verbose_name='Удалено'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время и дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время и дата обновления'
    )

    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None
    )

    class Meta:
        ordering = ['-id']

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.summary
