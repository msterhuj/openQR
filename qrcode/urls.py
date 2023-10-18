from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r"^q/(?P<qrcode_uuid>[0-9a-f-]+)$", views.fetch, name="qrcode_fetch"),
]
