import datetime

from django.core.exceptions import BadRequest
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from HSEPythonDev.src.core.models import Meeting, User
from HSEPythonDev.src.core.serializers import HelloWorldTextUpdateSerializer, AddMeetingSerializer


class ValidationViewSet(ViewSet):
    @staticmethod
    def validate(clazz, request=None):
        data = request.query_params if request.method == 'GET' else request.data
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


class MeetingsViewSet(ValidationViewSet):
    authentication_classes = ()
    permission_classes = ()

    def list(self, request):
        meetings = Meeting.objects.all()
        result = []
        for meeting in meetings:
            result.append({'name': meeting.name})

    def create(self, request):
        data = self.validate(AddMeetingSerializer, request)
        logins = [user['login'] for user in data.get('participants', [])]
        meeting = Meeting(start_time=datetime.time(), end_time=datetime.time(), name=data.get('name'), users=logins)
        meeting.save()
        return Response({'ok': True})


    def destroy(self):
        pass