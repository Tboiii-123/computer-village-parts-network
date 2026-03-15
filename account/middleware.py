from django.utils import timezone
from datetime import timedelta


class LastActiveMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if request.user.is_authenticated:
            profile = request.user.profile

            if not profile.last_active or timezone.now() - profile.last_active > timedelta(minutes=5):
                profile.last_active = timezone.now()
                profile.save(update_fields=["last_active"])

        return response