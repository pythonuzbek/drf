from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import Product, Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductModelSerializer(ModelSerializer):
    # category = CategoryModelSerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, value):
        if not value['category'].isdigit():
            raise ValidationError('this')
        return value

    def validate_name(self, value):
        if not value.isdigit():
            raise ValidationError('this is not  umber')
        return value
