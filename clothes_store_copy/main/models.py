from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.
#pw - maxim

class Availability(models.Model):
    name = models.CharField("Наличие одежды", max_length=50)
    url = models.SlugField(default='None', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Полы"


class Size(models.Model):
    name = models.CharField('Размер', max_length=30)
    url = models.SlugField(default='None', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

class Season(models.Model):
    name = models.CharField('Сезон', max_length=30)
    url = models.SlugField('url-адресс', max_length=150)

    class Meta:
        verbose_name = "Сезон"
        verbose_name_plural = "Сезоны"

    def __str__(self):
        return self.name

class Clothes(models.Model):
    image = models.ImageField("Фото", upload_to='')
    name = models.CharField('Название', max_length=100)
    contacts = models.TextField('контакты владельца товара', max_length=100, default='отсутствуют')
    sex = models.TextField("Пол", max_length=15)
    cost = models.PositiveSmallIntegerField('Цена', help_text='цена в сумах')
    seasons = models.ManyToManyField(Season, verbose_name='сезон', related_name='season')
    url = models.SlugField('url-адрес',max_length=100, unique=True, default='None')
    size = models.ManyToManyField(Size, verbose_name='размер', related_name='size')
    availability = models.ManyToManyField(Availability, verbose_name='наличие товара', related_name='availability')
    # if availability:
    #     availability = 'Имеется в наличии'
    # else:
    #     availability = 'Нет в наличии'

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"

    def get_season_url(self):
        return reverse('clothes',args=[self.seasons.name])

    def get_absolute_url(self):
        return reverse('clothes_detail',args=[self.url])

class Review(models.Model):
    name = models.CharField('Никнейм', max_length=30)
    text = models.TextField('отзыв', max_length=300)
    email = models.EmailField('Эл.почта')
    # reset = models.CharField('Сбросить', max_length=30, default="Сбросить")
    # cloth = models.ForeignKey(Clothes, on_delete=models.CASCADE, verbose_name="отзыв", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class User(models.Model):
    name = models.CharField("имя пользователя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

