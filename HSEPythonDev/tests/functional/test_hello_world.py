import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HSEPythonDev.settings')
from HSEPythonDev.src.testutils import MyTestCase


class TestHeloWorld(MyTestCase):
    def setUp(self) -> None:
        super(TestHeloWorld, self).setUp()
    
    def test_get(self):
        response = self.client.get('/test/hello/hello_world/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['message'], 'Hello, world!')

    def test_post(self):
        data = {'text': 'bye bye, world'}
        response = self.client.post('/test/hello/hello_world/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['message']['text'], 'bye bye, world')

    def test_multiple_get_and_post(self):
        for i in range(10):
            response = self.client.get('/test/hello/hello_world/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.content)['message'], 'Hello, world!')
            data = {'text': f'bye bye, world{i}'}
            response = self.client.post('/test/hello/hello_world/', data=data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.content)['message']['text'], f'bye bye, world{i}')
