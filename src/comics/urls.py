from django.urls import include, path
from rest_framework.routers import SimpleRouter

from comics.api import viewsets

router = SimpleRouter()
router.register('', viewsets.ComicViewSet)

default_name = 'comics'
urlpatterns = [
    path('', include(router.urls)),
]
