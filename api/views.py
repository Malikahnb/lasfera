from rest_framework.generics import ListAPIView

from api.serializers import ProductModelSerializer
from product.models import ProductModel


class ProductModelListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer

