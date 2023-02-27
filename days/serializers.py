from rest_framework import serializers
from .models import Training, Count


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = (
            "id",
            "name",
            "number",
            "icon",
        )


class CountSerializer(serializers.ModelSerializer):
    training = serializers.StringRelatedField()

    class Meta:
        model = Count
        fields = (
            "training",
            "number",
            "date",
        )
