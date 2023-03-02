from rest_framework import serializers
from .models import Health, Count


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = (
            "id",
            "health",
            "icon",
            "color",
        )


class CountSerializer(serializers.ModelSerializer):
    health = serializers.StringRelatedField()

    class Meta:
        model = Count
        fields = (
            "id",
            "date",
            "health",
            "count",
        )
