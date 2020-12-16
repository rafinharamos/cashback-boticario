from rest_framework import serializers

from sales.models import Sale


class CreateSalesSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True)
    value = serializers.FloatField(required=True)
    date = serializers.DateField(required=True)

    class Meta:
        model = Sale
        fields = ("code", "date", "value")

    def validate_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("Value must be bigger than 0")
        return value

    def validate_code(self, value):
        if Sale.objects.filter(code=value).exists():
            raise serializers.ValidationError("Sale with this code already exists")
        elif len(value) < 8 or len(value) > 9:
            raise serializers.ValidationError("Code must contain 8 digits")
        return value


class ListSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = (
            "code",
            "value",
            "date",
            "cashback_percent",
            "cashback_value",
            "status",
        )
