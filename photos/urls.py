from rest_framework.routers import DefaultRouter

from photos.views import PhotoViewSet, PhotoPeopleNamesViewSet

router = DefaultRouter()
router.register("photos", PhotoViewSet)
router.register("names", PhotoPeopleNamesViewSet)

urlpatterns = router.urls
