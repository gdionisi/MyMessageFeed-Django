from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from my_api.views import UserViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, base_name="user")
router.register(r'message', MessageViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]