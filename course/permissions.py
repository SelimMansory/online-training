from rest_framework.permissions import BasePermission


class IsStaffViewSet(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['list',]:
            return request.user.is_authenticated
        elif view.action == 'create':
            return request.user.group == 'user' or request.user.is_superuser
        elif view.action in ['update', 'retrieve']:
            return request.user == obj.owner or request.user.group == 'staff'
        elif view.action == 'destroy':
            return request.user == obj.owner
        else:
            return request.user.is_superuser


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True


class IsUser(BasePermission):

    def has_permission(self, request, view):
        return request.user.group == 'user'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner