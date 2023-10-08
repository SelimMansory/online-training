from rest_framework.permissions import BasePermission


class IsSameUser(BasePermission):

    def has_permission(self, request, view):
        print(view.user)
        return request.user.group == 'user'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner