from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор по пользователям"""

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "password", "country")
        extra_kwargs = {'password': {'write_only': True}}

class UserResetPassword(ModelSerializer):
    """Сериалайзер для сброса пароля"""

    class Meta:
        model = User
        fields = ("email",)
