from django.contrib.auth.models import Group
from django.db import transaction
from mozilla_django_oidc import auth


class OIDCAuthenticationBackend(auth.OIDCAuthenticationBackend):

    def create_user(self, claims):
        try:
            email = claims.get("email")
            username = claims.get('preferred_username', '')
            user = self.UserModel.objects.create_user(username, email=email)
            user.save()
        except Exception as e:
            raise Exception(e)
        return user

    def update_user(self, user, claims):
        # Update user
        return user
    