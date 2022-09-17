from django.core.exceptions import BadRequest
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from HSEPythonDev.src.core.serializers import HelloWorldTextUpdateSerializer


class ValidationViewSet(ViewSet):
    @staticmethod
    def validate(clazz, request=None):
        data = request.query_params if request.method == 'GET'\
            else request.data
        serializer = clazz(data=data, context={'request': request})
        if not serializer.is_valid():
            raise BadRequest(serializer.errors)
        return serializer.validated_data


class HelloWorldViewSet(ValidationViewSet):
    authentication_classes = ()
    permission_classes = ()
    text = 'Hello, world!'

    @action(url_path='hello_world', methods=['get', 'post'], detail=False)
    def handle_hello(self, request):
        if request.method == 'POST':
            self.text = self.validate(HelloWorldTextUpdateSerializer, request)
        return Response({'message': self.text})
