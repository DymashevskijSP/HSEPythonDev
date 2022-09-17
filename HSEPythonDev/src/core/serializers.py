from rest_framework import serializers


class HelloWorldTextUpdateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
