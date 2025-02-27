# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Clothes
# from .serializers import ClothesSerializer

# @api_view(['GET', 'POST'])
# def clothes_list(request):
#     if request.method == 'GET':
#         clothes = Clothes.objects.all()
#         serializer = ClothesSerializer(clothes, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = ClothesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def clothes_detail(request, pk):
#     try:
#         clothes = Clothes.objects.get(id=pk)
#     except Clothes.DoesNotExist:
#         return Response({'error': 'Clothes not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ClothesSerializer(clothes)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = ClothesSerializer(clothes, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         clothes.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# clothes/views.py
# from rest_framework import viewsets, pagination
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Clothes
# from .serializers import ClothesSerializer

# class ClothesPagination(pagination.PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100

#     def get_paginated_response(self, data):
#         return Response({
#             'count': self.page.paginator.count,
#             'total_pages': self.page.paginator.num_pages,
#             'current_page': self.page.number,
#             'results': data
#         })

# class ClothesViewSet(viewsets.ViewSet):
#     def list(self, request):
#         clothes = Clothes.objects.all()

#         # Filter by stock
#         stock = request.query_params.get('stock')
#         if stock:
#             clothes = clothes.filter(stock=stock)

#         # Sort by field with direction
#         sort_field = request.query_params.get('ordering', 'name')
#         if sort_field.lstrip('-') in ['name', 'price', 'stock']:
#             clothes = clothes.order_by(sort_field)

#         paginator = ClothesPagination()
#         result_page = paginator.paginate_queryset(clothes, request)
#         serializer = ClothesSerializer(result_page, many=True)
#         return paginator.get_paginated_response(serializer.data)

#     def create(self, request):
#         serializer = ClothesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         try:
#             clothes = Clothes.objects.get(id=pk)
#             serializer = ClothesSerializer(clothes)
#             return Response(serializer.data)
#         except Clothes.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def update(self, request, pk=None):
#         try:
#             clothes = Clothes.objects.get(id=pk)
#             serializer = ClothesSerializer(clothes, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Clothes.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def destroy(self, request, pk=None):
#         try:
#             clothes = Clothes.objects.get(id=pk)
#             clothes.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Clothes.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)


from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Clothes
from .serializers import ClothesSerializer
from rest_framework.pagination import PageNumberPagination
from base.permissions import IsSellerOrReadOnly

class ClothesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    pagination_class = ClothesPagination
    permission_classes = [IsSellerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['stock', 'size', 'color']
    ordering_fields = ['name', 'price', 'stock', 'size', 'color']
    ordering = ['name']

    def get_queryset(self):
        return Clothes.objects.filter(seller_id=self.request.user.id)

