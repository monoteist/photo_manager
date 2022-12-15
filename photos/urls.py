from rest_framework.routers import DefaultRouter

from photos.views import PhotoViewSet

router = DefaultRouter()
router.register('photos', PhotoViewSet)

urlpatterns = router.urls
