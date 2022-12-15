from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='photos/')
    location = models.CharField('Гео локация', max_length=255, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    people_names = models.ManyToManyField('PhotoPeopleName', blank=True)

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

class PhotoPeopleName(models.Model):
    name = models.CharField('Имя', max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Имя человека на фотографии'
        verbose_name_plural = 'Имена людей на фотографиях'