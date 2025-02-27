from rest_framework import permissions

from rest_framework import permissions


class AuthorOrForbidden(permissions.BasePermission):
    """
    1) Если пользователь не авторизован
    (request.user.is_authenticated == False),
       возвращаем 401 Unauthorized.
    2) Если пользователь авторизован, но пытается
    изменить чужой объект (PUT, PATCH, DELETE),
       возвращаем 403 Forbidden.
    3) Автор объекта может менять его.
    4) Авторизованный пользователь может читать
    (GET) любой объект.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, "author", None) == request.user


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
