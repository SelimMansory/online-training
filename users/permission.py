from rest_framework.permissions import BasePermission


class IsUser(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action == 'create':
            return True
        elif view.action in ['list', 'retrieve']:
            return request.user.is_authenticated
        elif view.action == 'update':
            return request.user == obj.owner
        else:
            return request.user.is_superuser