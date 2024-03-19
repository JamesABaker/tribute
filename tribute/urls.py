from django.contrib import admin
from django.urls import path

from tribute.views import HomePageView  # Import necessary views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
]
