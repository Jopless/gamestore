from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False, verbose_name='Название новости')
    text = models.TextField(null=False, blank=False, verbose_name='Текст')
    image = models.ImageField(upload_to='news_photos/%Y/%m/%d/', blank=True, verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    publish_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):

        return self.title

