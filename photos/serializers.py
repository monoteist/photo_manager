from rest_framework.serializers import ModelSerializer

from photos.models import Photo, PhotoPeopleName


class PhotoPeopleNameSerializer(ModelSerializer):
    class Meta:
        model = PhotoPeopleName
        fields = ("name",)


class PhotoCreateSerializer(ModelSerializer):
    people_names = PhotoPeopleNameSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ("photo", "location", "description", "people_names")
        extra_kwargs = {
            "location": {"required": False},
            "description": {"required": False},
            "people_names": {"required": False},
        }


class PhotoReadOnlySerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ("id", "photo")


class PhotoReadOnlyRetriveSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ("id", "photo", "location", "description", "people_names")
