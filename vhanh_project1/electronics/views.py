# from rest_framework import viewsets
# from .models import Electronics
# from .serializers import ElectronicsSerializer

# class ElectronicsViewSet(viewsets.ModelViewSet):
#     queryset = Electronics.objects.all()
#     serializer_class = ElectronicsSerializer


# # electronics/views.py
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.exceptions import ValidationError
# from .models import Electronics
# from .serializers import ElectronicsSerializer
# import json

# # Lấy danh sách hoặc tạo mới
# @csrf_exempt
# def electronics_list(request):
#     if request.method == 'GET':
#         electronics = Electronics.objects.all()
#         data = [ElectronicsSerializer.serialize(e) for e in electronics]
#         return JsonResponse(data, safe=False)

#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             valid_data = ElectronicsSerializer.deserialize(data)
#             electronic = Electronics.objects.create(**valid_data)
#             return JsonResponse(ElectronicsSerializer.serialize(electronic), status=201)
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': 'Dữ liệu không hợp lệ'}, status=400)

# # Chi tiết, cập nhật, xóa
# @csrf_exempt
# def electronics_detail(request, pk):
#     try:
#         electronic = Electronics.objects.get(pk=pk)
#     except Electronics.DoesNotExist:
#         return JsonResponse({'error': 'Không tìm thấy sản phẩm'}, status=404)

#     if request.method == 'GET':
#         return JsonResponse(ElectronicsSerializer.serialize(electronic))

#     if request.method == 'PUT':
#         try:
#             data = json.loads(request.body)
#             valid_data = ElectronicsSerializer.deserialize(data)

#             for key, value in valid_data.items():
#                 setattr(electronic, key, value)
#             electronic.save()

#             return JsonResponse(ElectronicsSerializer.serialize(electronic))
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     if request.method == 'DELETE':
#         electronic.delete()
#         return JsonResponse({'message': 'Xóa thành công'}, status=204)


# electronics/views.py
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.exceptions import ValidationError, PermissionDenied
# from django.contrib.auth.decorators import login_required
# from .models import Electronics
# from .serializers import ElectronicsSerializer
# import json
# from base.authentication import CustomJWTAuthentication

# def check_permission(request, electronic=None):
#     """ Kiểm tra quyền của user """
#     # if request.user.is_superuser:
#     #     return  # Admin toàn quyền

#     if request.method in ('GET', 'HEAD', 'OPTIONS'):
#         if hasattr(request.user, 'customer_type'):
#             return  # Customer được phép GET
#         if electronic and electronic.seller_id == request.user.id:
#             return  # Seller chỉ GET sản phẩm của chính họ

#     if hasattr(request.user, 'shop_name'):
#         if electronic and electronic.seller_id == request.user.id:
#             return  # Seller chỉ CRUD sản phẩm của mình

#     raise PermissionDenied("Bạn không có quyền thao tác trên sản phẩm này.")

# @csrf_exempt
# def electronics_list(request):
#     jwt_authenticator = CustomJWTAuthentication()
#     user, _ = jwt_authenticator.authenticate(request)
#     request.user = user

#     print(f"User: {request.user}")
#     print(f"Is Authenticated: {request.user.is_authenticated}")
#     if request.method == 'GET':
#         print(request.user)
#         if request.user.is_superuser:
#             electronics = Electronics.objects.all()
#         elif hasattr(request.user, 'shop_name'):
#             electronics = Electronics.objects.filter(seller_id=request.user.id)
#         else:
#             return JsonResponse({'error': 'Bạn không có quyền xem danh sách này'}, status=403)

#         data = [ElectronicsSerializer.serialize(e) for e in electronics]
#         return JsonResponse(data, safe=False)

#     if request.method == 'POST':
#         if not hasattr(request.user, 'shop_name'):
#             return JsonResponse({'error': 'Chỉ seller mới có thể tạo sản phẩm'}, status=403)

#         try:
#             data = json.loads(request.body)
#             valid_data = ElectronicsSerializer.deserialize(data)
#             valid_data['seller_id'] = request.user.id  # Gán seller_id khi tạo
#             electronic = Electronics.objects.create(**valid_data)
#             return JsonResponse(ElectronicsSerializer.serialize(electronic), status=201)
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': 'Dữ liệu không hợp lệ'}, status=400)

# @csrf_exempt
# def electronics_detail(request, pk):
#     """ Lấy chi tiết, cập nhật, xóa sản phẩm """
#     try:
#         electronic = Electronics.objects.get(pk=pk)
#     except Electronics.DoesNotExist:
#         return JsonResponse({'error': 'Không tìm thấy sản phẩm'}, status=404)

#     try:
#         check_permission(request, electronic)
#     except PermissionDenied as e:
#         return JsonResponse({'error': str(e)}, status=403)

#     if request.method == 'GET':
#         return JsonResponse(ElectronicsSerializer.serialize(electronic))

#     if request.method == 'PUT':
#         try:
#             data = json.loads(request.body)
#             valid_data = ElectronicsSerializer.deserialize(data)

#             for key, value in valid_data.items():
#                 setattr(electronic, key, value)
#             electronic.save()

#             return JsonResponse(ElectronicsSerializer.serialize(electronic))
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     if request.method == 'DELETE':
#         electronic.delete()
#         return JsonResponse({'message': 'Xóa thành công'}, status=204)


# electronics/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError, PermissionDenied
from .models import Electronics
from .serializers import ElectronicsSerializer
import json
from base.authentication import CustomJWTAuthentication
from django.core.paginator import Paginator

def check_permission(request, electronic=None):
    """ Kiểm tra quyền của user """
    if request.user.is_superuser:
        return  # Admin toàn quyền

    if request.method in ('GET', 'HEAD', 'OPTIONS'):
        if hasattr(request.user, 'customer_type'):
            return  # Customer được phép GET
        if electronic and electronic.seller_id == request.user.id:
            return  # Seller chỉ GET sản phẩm của chính họ

    if hasattr(request.user, 'shop_name'):
        if electronic and electronic.seller_id == request.user.id:
            return  # Seller chỉ CRUD sản phẩm của mình

    raise PermissionDenied("Bạn không có quyền thao tác trên sản phẩm này.")

@csrf_exempt
def electronics_list(request):
    """ Lấy danh sách hoặc tạo sản phẩm với paging, sort và filter """
    jwt_authenticator = CustomJWTAuthentication()
    user, _ = jwt_authenticator.authenticate(request)
    request.user = user

    print(f"User: {request.user}")
    print(f"Is Authenticated: {request.user.is_authenticated}")

    if request.method == 'GET':
        if request.user.is_superuser:
            electronics = Electronics.objects.all()
        elif hasattr(request.user, 'shop_name'):
            electronics = Electronics.objects.filter(seller_id=request.user.id)

        # Lọc theo tên
        name = request.GET.get('name')
        if name:
            electronics = electronics.filter(name__icontains=name)

        # Sắp xếp
        sort_by = request.GET.get('sort_by', 'name')  # Mặc định sort theo name
        if sort_by not in ('name', 'price', 'stock'):
            sort_by = 'name'
        order = request.GET.get('order', 'asc')
        if order == 'desc':
            sort_by = f'-{sort_by}'
        electronics = electronics.order_by(sort_by)

        # Phân trang
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 5))
        paginator = Paginator(electronics, page_size)
        current_page = paginator.get_page(page)

        data = [ElectronicsSerializer.serialize(e) for e in current_page]
        return JsonResponse({
            'results': data,
            'total_pages': paginator.num_pages,
            'current_page': current_page.number,
            'total_items': paginator.count
        }, safe=False)

    if request.method == 'POST':
        if not hasattr(request.user, 'shop_name'):
            return JsonResponse({'error': 'Chỉ seller mới có thể tạo sản phẩm'}, status=403)

        try:
            data = json.loads(request.body)
            valid_data = ElectronicsSerializer.deserialize(data)
            valid_data['seller_id'] = request.user.id  # Gán seller_id khi tạo
            electronic = Electronics.objects.create(**valid_data)
            return JsonResponse(ElectronicsSerializer.serialize(electronic), status=201)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Dữ liệu không hợp lệ'}, status=400)

@csrf_exempt
def electronics_detail(request, pk):
    """ Lấy chi tiết, cập nhật, xóa sản phẩm """
    try:
        electronic = Electronics.objects.get(pk=pk)
    except Electronics.DoesNotExist:
        return JsonResponse({'error': 'Không tìm thấy sản phẩm'}, status=404)

    jwt_authenticator = CustomJWTAuthentication()
    user, _ = jwt_authenticator.authenticate(request)
    request.user = user

    try:
        check_permission(request, electronic)
    except PermissionDenied as e:
        return JsonResponse({'error': str(e)}, status=403)

    if request.method == 'GET':
        return JsonResponse(ElectronicsSerializer.serialize(electronic))

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            valid_data = ElectronicsSerializer.deserialize(data)

            for key, value in valid_data.items():
                setattr(electronic, key, value)
            electronic.save()

            return JsonResponse(ElectronicsSerializer.serialize(electronic))
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'DELETE':
        electronic.delete()
        return JsonResponse({'message': 'Xóa thành công'}, status=204)