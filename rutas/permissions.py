from rest_framework.permissions import BasePermission


class IsMyDevice(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.device == request.query_params.get('device')
