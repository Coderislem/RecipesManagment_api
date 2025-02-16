from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
