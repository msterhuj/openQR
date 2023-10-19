from django.urls import path

from .views import index_view, register_view, login_view, logout_view

urlpatterns = [
    path("", index_view, name="dashboard_index"),
    path("login/", login_view, name="dashboard_login"),
    path("register/", register_view, name="dashboard_register"),
    path("logout/", logout_view, name="dashboard_logout"),
]
