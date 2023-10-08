from rest_framework.permissions import BasePermission


class IsUser(BasePermission):

    def has_permission(self, request, view):
        if view.action == ['create', 'list']:
            return True
        else:
            return request.user.is_authenticated


class IsPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'retrieve']:
            return request.user.email == obj.email
        else:
            return request.user.is_superuser