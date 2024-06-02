from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from django.contrib.auth.models import AbstractUser
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
