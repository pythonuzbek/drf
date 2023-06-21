from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.models import Product, Category
from apps.serializers import ProductModelSerializer, CategoryModelSerializer


# class ProductAPIView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductModelSerializer(products, many=True)
#         return Response(serializer.data)
#
#     @swagger_auto_schema(request_body=ProductModelSerializer)
#     def post(self, request):
#         product = ProductModelSerializer(data=request.data)
#         product.is_valid(raise_exception=True)
#         product.save()
#         return Response(product.data)

#
class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    # def get(self, request):
    #     categories = Category.objects.all()
    #     serializer = CategoryModelSerializer(categories,many=True)
    #     return Response(serializer.data)


# class ProductAPIView(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer
#
#     @action(detail=False, methods=["GET"])
#     def top(self, request, *args, **kwargs):
#         products = self.get_queryset()
#         products = products.order_by('-price')[:5]
#         serializer = ProductModelSerializer(products,many=True)
#         return Response(serializer.data)


# class ProductAPIView(APIView):
#     def post(self, request):
#         serializer = ProductModelSerializer(data=request.data)
#         serializer.is_valid()
#         serializer.save()
#         return Response(serializer.data)
