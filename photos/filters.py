import django_filters

from photos.models import Photo

class PhotoFilter(django_filters.FilterSet):
    class Meta:
        model = Photo
        fields = ['location', 'date', 'people_names', 'description']