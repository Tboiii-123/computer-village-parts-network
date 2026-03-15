from django.urls import path
from .views import create_item_request, get_all_requests, request_detail,update_request_status

urlpatterns = [
    path("create/", create_item_request),
    path("list/", get_all_requests),
    path("detail/<int:request_id>/", request_detail),
    path("<int:request_id>/update_request_status/", update_request_status),
]