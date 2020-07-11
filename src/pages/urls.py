from django.urls import include, path
from rest_framework.routers import SimpleRouter

from pages.api import viewsets as pages

router = SimpleRouter()
router.register('', pages.PageViewSet, basename='page')

app_name = 'pages'
urlpatterns = [
    path('', include(router.urls)),
]
