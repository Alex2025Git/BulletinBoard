import secrets

from django.core.mail import send_mail
from django.http import Http404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from config.settings import EMAIL_HOST_USER
from users.models import User
from users.serializers import UserResetPassword, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action in ["list", "retrieve", "update", "destroy"]:
            self.permission_classes = (IsAuthenticated & IsAdminUser,)
        return super().get_permissions()

    @staticmethod
    def reset_password(request):
        """Сброс пароля"""
        try:
            user = User.objects.get(email=request.data.get("email"))
        except User.DoesNotExist:
            raise Http404

        serializer = UserResetPassword(user, data=request.data)
        if serializer.is_valid():
            token = secrets.token_hex(16)
            user.token_for_password = token
            user.save()
            host = request.get_host()
            url = f"http://{host}/users/reset-password-confirm/{user.pk}/{user.token_for_password}/"
            send_mail(
                subject=f"Сброс пароля для {User.objects.get(email=user.email)}",
                message=f"Для сброса пароля отправьте запрос по ссылке {url}, "
                f'указав новый пароль в теле: "new_password": "******"',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            return Response(f"Данные для сброса направлены Вам на почту {request.data.get('email')}")
        return Http404

    @staticmethod
    def reset_password_confirm(request, pk, token):
        """Подтверждение сброса пароля"""
        try:
            user = User.objects.get(pk=pk, token_for_password=token)
        except User.DoesNotExist:
            raise Http404

        new_password = request.data.get("new_password")
        user.set_password(new_password)
        user.save()
        return Response("Пароль успешно изменен")
