from rest_framework import serializers
from .models import Message, MessagePerson


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "text", "timestamp",]

    def validate_text(self, value):
        if Message.objects.filter(text=value).exists():
            raise serializers.ValidationError("Duplicate message detected")
        return value

class MessagePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagePerson
        fields = ["id", "name", "lastname",]

    def validate_name(self, value):
        if MessagePerson.objects.filter(name=value).exists():
            raise serializers.ValidationError("Duplicate message detected")
        return value