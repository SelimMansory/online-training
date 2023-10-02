from rest_framework.permissions import BasePermission


class IsStaffViewSet(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'create', ]:
            return request.user.is_authenticated
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


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(view.action)
        return request.user == obj.owner