from django.db import models

# Create your models here.
game_rate = (
    ('1', "1"),
    ('2', "2"),
    ('3', "3"),
    ('4', "4"),
    ('5', "5"),
)


class Game(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=False, verbose_name="Название игры")
    price = models.FloatField(null=False, blank=False, unique=False, verbose_name="Цена")
    description = models.TextField(blank=False, null=True, verbose_name="Описание игры")
    rating = models.CharField(max_length=1, choices=game_rate)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Фото")
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):

        return self.title
