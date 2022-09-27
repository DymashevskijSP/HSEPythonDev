from rest_framework.test import APIClient, APITransactionTestCase
from django.core.wsgi import get_wsgi_application
from unittest import TestCase
application = get_wsgi_application()


class MyTestCase(APITransactionTestCase, TestCase):
    client_class = APIClient
