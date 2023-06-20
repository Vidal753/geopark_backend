from django.urls import path, include
from rest_framework import routers
from backend.views import (
    CityViewSet,
    NewsViewSet,
    DocumentViewSet,
    ImageViewSet,
    VideoViewSet,
)

router = routers.DefaultRouter()
router.register(r"city", CityViewSet)
router.register(r"news", NewsViewSet)
router.register(r"documents", DocumentViewSet)
router.register(r"images", ImageViewSet)
router.register(r"videos", VideoViewSet)


urlpatterns = [path("", include(router.urls))]
