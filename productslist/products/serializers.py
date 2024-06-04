from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(default="Category")

    class Meta:
        model = models.Product
        fields = (
            "id",
            "name",
            "creation_date",
            "category",
            "description",
            "number_of_items",
            "price",
        )
        read_only_fields = ("creation_date",)
