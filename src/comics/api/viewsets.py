from rest_framework.viewsets import ReadOnlyModelViewSet

from comics.api.serializers import ComicSerializer
from comics.models import Comic


class ComicViewSet(ReadOnlyModelViewSet):
    serializer_class = ComicSerializer
    queryset = Comic.objects.all()
    lookup_field = 'slug'
