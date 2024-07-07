from rest_framework import permissions
from .apps import answer


class OnlyAuthorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if bool(answer) is True:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

