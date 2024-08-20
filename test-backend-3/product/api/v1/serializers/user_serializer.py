from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import Subscription, Balance

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = User
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    class BalanceSerializer(serializers.Serializer):
        class Meta:
            model = Balance
            fields = '__all__'

    class Meta:
        model = Subscription
        fields = (
            '__all__'
        )
