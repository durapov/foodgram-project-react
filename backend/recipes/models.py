from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator, MinValueValidator
from django.db import models

from backend.constants import MAX_NAME_LENGTH, MAX_EMAIL_LENGTH


class User(AbstractUser):
    """User model"""
    REQUIRED_FIELDS = ('username', 'last_name', 'first_name',)
    USERNAME_FIELD = 'email'

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
    )

    username = models.CharField(
        verbose_name='Уникальный юзернэйм',
        max_length=MAX_NAME_LENGTH,
        validators=[UnicodeUsernameValidator()],
        unique=True,
        error_messages={
            'unique': 'Пользователь с таким именем уже существует.',
        }
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=MAX_NAME_LENGTH,
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=MAX_NAME_LENGTH,
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи',

    def __str__(self):
        return self.username


class Recipe(models.Model):
    tags = models.ManyToManyField(
        'Tag',
#        on_delete=models.CASCADE,
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
#        on_delete=models.CASCADE,
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

