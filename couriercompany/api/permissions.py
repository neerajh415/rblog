from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_permission(self, request, view, obj=None):
    # Write permissions are only allowed to the owner of the snippet
    	return obj is None or obj.from_user == request.user