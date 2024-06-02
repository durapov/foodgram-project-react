from rest_framework import serializers
from .models import User
from backend.constants import MAX_NAME_LENGTH
from .validators import username_validator

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""

    username = serializers.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[username_validator]
    )
    # is_subscribed = serializers.SerializerMethodField(read_omly=True)

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