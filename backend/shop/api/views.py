from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import ProductSerializer
from products.models import Product


class ProductsViewSet(ModelViewSet, CreateModelMixin, RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            price_details = e.detail.get("price")
            title_details = e.detail.get("title")
            message = ""
            if title_details:
                message += "Ошибки в названии:\n"
                for detail in title_details:
                    message += f"{detail}\n"
            if price_details:
                message += "Ошибки в цене:\n"
                for detail in price_details:
                    message += f"{detail}\n"
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message': "Произошла внутрення ошибка сервера"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
