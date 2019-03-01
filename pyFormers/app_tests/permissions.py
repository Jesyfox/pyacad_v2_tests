from rest_framework import permissions


class JWordUsersNotAllowed(permissions.BasePermission):
    message = 'Users with "j" not allowed!'

    def has_permission(self, request, view,):
        return not request.user.username.startswith('j')
