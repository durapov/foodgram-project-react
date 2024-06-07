from django.shortcuts import render
from rest_framework import viewsets
from djoser import views as djoser_views
from .models import Recipe, Tag, Ingredient, IngredientInRecipe, User
from .serializers import (RecipeSerializer, TagSerializer,
                          IngredientSerializer, IngredientInRecipeSerializer, UserSerializer)


class UserViewSet(djoser_views.UserViewSet):
    queryset = User.objects.all()
    srializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientInRecipeViewSet(viewsets.ModelViewSet):
    queryset = IngredientInRecipe.objects.all()
    serializer_class = IngredientInRecipeSerializer
