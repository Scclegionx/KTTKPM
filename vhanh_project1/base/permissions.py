from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsSellerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # In ra thông tin user và token
        print(f"User: {request.user}, Auth Backend: {getattr(request.user, 'backend', None)}")
        print(f"User: {request.user}, User Type: {request.user.__class__}, Auth: {request.auth}")
    
        if hasattr(request.user, 'shop_name'):
            return True

        if hasattr(request.user, 'customer_type') and request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        if request.user.is_superuser:
            return True

    
    def has_object_permission(self, request, view, obj):
        # print(f"User: {request.user}, Auth Backend: {getattr(request.user, 'backend', None)}")
        # print(f"User: {request.user}, User Type: {request.user.__class__}, Auth: {request.auth}")

        if hasattr(request.user, 'customer_type') and request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        if hasattr(request.user, 'shop_name') and obj.seller_id == request.user.id:
            return True

        if request.user.is_superuser:
            return True

        raise PermissionDenied("Bạn không có quyền thao tác trên sản phẩm này.")
