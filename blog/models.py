from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок категории')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название местоположения')

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )
    # image удалено, чтобы не требовался Pillow

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
    