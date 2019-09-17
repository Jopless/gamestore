from django.db import models
from django.utils import timezone

# Create your models here.
game_rate = (
    ('★☆☆☆☆', "1"),
    ('★★☆☆☆', "2"),
    ('★★★☆☆', "3"),
    ('★★★★☆', "4"),
    ('★★★★★', "5"),
)

game_genre = (
    ('Sports', 'Sports'),
    ('Shooters', 'Shooters'),
    ('Racing', 'Racing'),
)

class Game(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=False, verbose_name="Название игры")
    price = models.FloatField(null=False, blank=False, unique=False, verbose_name="Цена")
    description = models.TextField(blank=False, null=True, verbose_name="Описание игры")
    rating = models.CharField(max_length=255, choices=game_rate)
    genre = models.CharField(max_length=255, choices=game_genre, null=True)
    release_date = models.DateTimeField(default=timezone.now, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False, verbose_name="Фото обложки")
    screenshot_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Доп. скриншот 1")
    screenshot_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Доп. скриншот 2")
    screenshot_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Доп. скриншот 3")
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):

        return self.title
