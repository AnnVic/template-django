from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import User
from typing import Any


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request: Any, view: Any) -> Any:
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request: Any, view: Any, obj: Any) -> Any:
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user