from rest_framework import serializers

from comics.models.comic import Comic
from users.api.serializers import UserSerializer


class ComicSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Comic
        fields = ['slug', 'owner']
