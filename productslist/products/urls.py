from rest_framework import routers

from . import viewsets

router = routers.SimpleRouter()
router.register(r"product", viewsets.ProductViewSet)

urlpatterns = [
    *router.urls,
]
