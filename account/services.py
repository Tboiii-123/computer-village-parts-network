from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from google.auth.transport import requests
from google.oauth2 import id_token
from google.auth.exceptions import GoogleAuthError



User = get_user_model()

#We crated a class classed GoogleAuthService 
class GoogleAuthService:
      #You can call the method without creating an object. staticmethod
      # service = GoogleAuthService()
    #service.verify_google_token(token)  
    #We do
    # GoogleAuthService.verify_google_token(token)
    @staticmethod
    def verify_google_token(token: str):
        """
        Verify Google token securely.
        """

        try:
            payload = id_token.verify_oauth2_token(
                token,
                requests.Request(),
                settings.GOOGLE_CLIENT_ID
            )

            # Verify issuer
            #iss means:

# issuer

# You're checking:

# Was this token actually issued by Google?

            if payload["iss"] not in [
                "accounts.google.com",
                "https://accounts.google.com"
            ]:
                raise ValueError("Invalid issuer")

            # Verify audience
            if payload["aud"] != settings.GOOGLE_CLIENT_ID:
                raise ValueError("Invalid audience")

            return payload

        except Exception as e:
            print("GOOGLE ERROR:", str(e))
            raise ValueError(str(e))
            

    @staticmethod
    #Using transaction here either eerything succeeds or roll back
    @transaction.atomic
    def create_or_update_user(payload):
        """
        Create or update Google user.
        """

        email = payload.get("email")
        email_verified = payload.get("email_verified", False)

        if not email or not email_verified:
            raise ValueError("Google email not verified")

        full_name = payload.get("name", "")
        first_name = ""
        last_name = ""

        if full_name:
            split_name = full_name.split()
            first_name = split_name[0]
            last_name = " ".join(split_name[1:])

        picture = payload.get("picture", "")

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "user_name": email,
                "first_name": first_name,
                "last_name": last_name,
                "is_approved": True,
            }
        )

        # Update fields only if changed
        fields_to_update = []

        if user.first_name != first_name:
            user.first_name = first_name
            fields_to_update.append("first_name")

        if user.last_name != last_name:
            user.last_name = last_name
            fields_to_update.append("last_name")

        if fields_to_update:
            user.save(update_fields=fields_to_update)

        return user