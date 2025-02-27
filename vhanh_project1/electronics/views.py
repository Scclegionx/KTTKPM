# from rest_framework import viewsets
# from .models import Electronics
# from .serializers import ElectronicsSerializer

# class ElectronicsViewSet(viewsets.ModelViewSet):
#     queryset = Electronics.objects.all()
#     serializer_class = ElectronicsSerializer


# electronics/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import Electronics
from .serializers import ElectronicsSerializer
import json

# Lấy danh sách hoặc tạo mới
@csrf_exempt
def electronics_list(request):
    if request.method == 'GET':
        electronics = Electronics.objects.all()
        data = [ElectronicsSerializer.serialize(e) for e in electronics]
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            valid_data = ElectronicsSerializer.deserialize(data)
            electronic = Electronics.objects.create(**valid_data)
            return JsonResponse(ElectronicsSerializer.serialize(electronic), status=201)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Dữ liệu không hợp lệ'}, status=400)

# Chi tiết, cập nhật, xóa
@csrf_exempt
def electronics_detail(request, pk):
    try:
        electronic = Electronics.objects.get(pk=pk)
    except Electronics.DoesNotExist:
        return JsonResponse({'error': 'Không tìm thấy sản phẩm'}, status=404)

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
