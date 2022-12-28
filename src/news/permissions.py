from typing import Any
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import APIView
from django.http import HttpRequest


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: HttpRequest, view: APIView) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(
        self, request: HttpRequest, view: APIView, obj: Any
    ) -> Any:
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
