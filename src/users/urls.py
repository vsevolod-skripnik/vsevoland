from django.urls import include, path
from rest_framework.routers import SimpleRouter

from users.api import viewsets

router = SimpleRouter()
router.register('', viewsets.UserViewSet)

app_name = 'users'
urlpatterns = [
    path('', include(router.urls)),
]
