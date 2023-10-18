from django.db import models
from django.contrib.auth.models import User


class QRCode(models.Model):
    uuid = models.UUIDField(unique=True, editable=False)
    data = models.CharField(max_length=255)
    disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
