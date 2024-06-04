from rest_framework import viewsets, permissions
from . import serializers
from . import models


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            category = self.request.query_params.get("category")
            if category:
                return queryset.filter(category=category)
        return queryset
