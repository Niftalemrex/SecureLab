from rest_framework.permissions import BasePermission


class IsTechnician(BasePermission):
    """
    Allows access only to authenticated users
    whose role is TECHNICIAN.
    """

    message = "Technician access required."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "TECHNICIAN"
        )