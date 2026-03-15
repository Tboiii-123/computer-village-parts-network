from django.urls import path
from .views import report_user

urlpatterns = [
    path("report/<int:user_id>/", report_user),
]