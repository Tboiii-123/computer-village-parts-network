from django.urls import path
from .views import i_have_it, request_responses

urlpatterns = [
    path("respond/<int:request_id>/", i_have_it),
    path("list/<int:request_id>/", request_responses),
]