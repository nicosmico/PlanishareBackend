import os
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework import exceptions
from firebase_admin import auth, initialize_app, credentials

from planishare.settings import BASE_DIR

User = get_user_model() # To use custom user seted in settings

cred = credentials.Certificate(os.path.join(BASE_DIR, "firebase_config.json"))

initialize_app(cred)
class FirebaseBackend(authentication.BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.META.get("HTTP_AUTHORIZATION")
        if not authorization_header:
            raise exceptions.AuthenticationFailed('Authorization credentials not provided')

        id_token = authorization_header.split(" ").pop()
        if not id_token:
            raise exceptions.AuthenticationFailed('Authorization credentials not provided')

        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise exceptions.AuthenticationFailed('Invalid ID Token')

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise exceptions.AuthenticationFailed('No such user exists')
        
        try:
            email = decoded_token.get("email")
        except Exception:
            raise exceptions.AuthenticationFailed('Email user not found')
        
        # TODO: Add more fields
        user, created = User.objects.get_or_create(
            email=email
        )

        return (user, None)