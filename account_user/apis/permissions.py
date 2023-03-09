from rest_framework.permissions import BasePermission


class IsOwnerOfObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
