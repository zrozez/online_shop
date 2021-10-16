from rest_framework import routers

from .views import CategoryViewSet


router = routers.SimpleRouter()
router.register('category', CategoryViewSet)

urlpatterns = []

urlpatterns += router.urls
