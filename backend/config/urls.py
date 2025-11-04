from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from analyzer.views import GovernmentPortalViewSet, ScanResultViewSet

router = DefaultRouter()
router.register(r'portals', GovernmentPortalViewSet)
router.register(r'results', ScanResultViewSet, basename='result')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]