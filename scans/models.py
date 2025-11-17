from django.db import models
from django.conf import settings


class Scan(models.Model):
    MODALITY_CHOICES = [
        ('ct', 'CT Scan'),
        ('mri', 'MRI Scan'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scans')
    modality = models.CharField(max_length=10, choices=MODALITY_CHOICES)
    file = models.FileField(upload_to='scans/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # результат анализа – как JSON (проценты, стадия и т.д.), может быть null
    result = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_modality_display()} ({self.uploaded_at})"
