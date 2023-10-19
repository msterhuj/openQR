from django.db import models
from django.contrib.auth.models import User
import uuid as uuid_lib


class QRCode(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid_lib.uuid4, db_index=True)
    name = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{str(self.uuid)} - {self.data}"
