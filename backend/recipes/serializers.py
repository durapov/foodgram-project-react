from rest_framework import serializers

from .models import Recipe, Ingredient, Tag, IngredientInRecipe, User  # , User
from .validators import username_validator
from backend.constants import MAX_NAME_LENGTH


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""

    username = serializers.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[username_validator]
    )
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name'
#            'is_subscribed'
        )


class UserMeRoleSerializer(UserSerializer):
    role = serializers.CharField()


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'ingredients', 'is_favorited', 'is_in_shopping_cart',
                  'name', 'image', 'text', 'cooking_time')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name', 'measurment_unit')


class IngredientInRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientInRecipe
        fields = ('ingredient', 'recipe')


