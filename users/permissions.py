from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Проверяет, явыляется ли пользователь владельцем"""

        if request.user.is_staff:
            return True
        return request.user == obj.author


class IsAdmin(BasePermission):
    """
    Проверка прав доступа для пользователей с ролью "admin"
    """

    def has_permission(self, request, view):
        """
        Проверяет роль пользователя
        """
        return request.user.role == "admin"