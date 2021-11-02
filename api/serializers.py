from rest_framework import serializers

from product.models import ProductModel, CategoryModel, ColorModel, SizeModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = '__all__'


class SizeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    color = ColorModelSerializer(many=True)
    size = SizeModelSerializer(many=True)

    class Meta:
        model = ProductModel
        fields = '__all__'
        # exclude = ['']
