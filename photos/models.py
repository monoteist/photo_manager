from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    location = models.CharField('Гео локация', max_length=255)
    description = models.TextField('Описание')
    people_names = models.ManyToManyField('PhotoPeopleName')

    def __str__(self) -> str:
        return self.author + self.description

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