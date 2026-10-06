from rest_framework import serializers

from .models import LabTest


class LabTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = LabTest
        fields = [
            "id",
            "name",
            "description",
            "price",
            "is_active",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Price cannot be negative."
            )

        return value