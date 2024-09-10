from rest_framework import routers

from .views import ProductsViewSet

api_router = routers.SimpleRouter()

app_name = "api"

api_router.register(r'products', ProductsViewSet)

urlpatterns = api_router.urls
