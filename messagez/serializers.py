from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "text", "timestamp"]

    def validate_text(self, value):
        if Message.objects.filter(text=value).exists():
            raise serializers.ValidationError("Duplicate message detected")
        return value
