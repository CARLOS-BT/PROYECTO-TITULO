from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class RutBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(RUT=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None