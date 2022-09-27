from rest_framework import serializers


class HelloWorldTextUpdateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)


class UserSerializer(serializers.Serializer):
    login = serializers.CharField(required=False)


class AddMeetingSerializer(serializers.Serializer):
    start_time = serializers.CharField(required=True)
    end_time = serializers.CharField(required=True)
    participants = serializers.ListField(child=UserSerializer(), required=True)
    is_private = serializers.BooleanField(required=False, default=False)
