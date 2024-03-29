from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from . import serializers
from category.models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.action in ('retrive', 'list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
