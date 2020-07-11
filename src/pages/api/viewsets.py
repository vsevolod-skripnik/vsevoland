from app.api.viewsets import AppViewSet
from pages.api import serializers
from pages.models import Page


class PageViewSet(AppViewSet):
    serializer_class = serializers.PageSerializer
    queryset = Page.objects.all()
