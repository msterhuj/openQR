from django.shortcuts import render
from django.http import HttpResponse
import uuid as uuid_lib

from .models import QRCode


def fetch(request, qrcode_uuid):
    # Check if qrcode_uuid is a valid UUID
    try:
        uuid_lib.UUID(qrcode_uuid, version=4)
    except ValueError:
        return HttpResponse(status=404)

    # Get the QRCode object from the database
    # check if the QRCode exists
    try:
        qrcode = QRCode.objects.get(uuid=qrcode_uuid)
    except QRCode.DoesNotExist:
        return HttpResponse(status=404)
    # check if the QRCode is active
    if not qrcode.active:
        return HttpResponse(qrcode.data)
