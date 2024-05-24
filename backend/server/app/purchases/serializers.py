from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    token = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
