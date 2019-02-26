from django.contrib.auth.models import User
from django_dynamic_fixture import G
from rest_framework.authtoken.models import Token


def create_user(username=None, email=None, password=None):
    user = G(User)
    if email is not None:
        user.email = email
    if username is not None:
        user.username = username
    if password is not None:
        user.set_password(password)
    user.save()
    return user


def get_user_auth_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token.key
