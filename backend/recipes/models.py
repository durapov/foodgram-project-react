from django.core.validators import RegexValidator, MinValueValidator
from django.db import models

from backend.users.models import User


# Create your models here.
class Recipe(models.Model):
    tags = models.ManyToManyField(
        'Tag',
        on_delete=models.CASCADE,
        related_name='tags'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author'
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='IngredientInRecipe',
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    is_favorited = models.BooleanField('Находится ли в избранном')
    is_in_shopping_cart = models.BooleanField('Находится ли в корзине')
    name = models.CharField('Название', max_length=200)
    image = models.URLField('Ссылка на картинку на сайте')
    text = models.TextField('Описание')
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления (в минутах)',
        validators=[MinValueValidator(1)]
    )


class Tag(models.Model):
    name = models.CharField('Название', max_length=200)
    color = models.CharField('Цвет в HEX', max_length=7)
    slug = models.CharField(
        'Уникальный слаг',
        max_length=200,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[-a-zA-Z0-9_]+$',
            message='Неподходящий слаг')
        ]

    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Ingredient(models.Model):
    name = models.CharField('Название', max_length=200)
    measurment_unit = models.CharField('Единицы измерения', max_length=200)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        related_name='IngredientInRecipe',
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='IngredientInRecipe',
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Список ингредиентов'
        verbose_name_plural = 'Списки ингредиентов'

