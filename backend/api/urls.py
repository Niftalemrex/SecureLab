from django.urls import path

from .views import HealthCheckView, LabTestListView


urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path("tests/", LabTestListView.as_view(), name="lab-test-list"),
]