from rest_framework import permissions

from .models import User


# Checking if User is correct to give him access to personal information.
class IsAuthorUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.owner == request.user)


class IsOwnerOfPage(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.page.owner == request.user)


class IsUserAdm(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.role == User.Roles.ADMIN)



# Checking if User is Moderator to give him particular rights
class IsUserModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user == User.Roles.choices.MODERATOR)
