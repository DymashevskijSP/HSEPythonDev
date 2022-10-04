import json
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HSEPythonDev.settings')
from HSEPythonDev.src.testutils import MyTestCase


class TestHeloWorld(MyTestCase):
    def setUp(self) -> None:
        super(TestHeloWorld, self).setUp()

    def test_post(self):
        data = {
            'start_time': '10:11:00 2122.09.27',
            'end_time': '11:11:00 2122.09.27',
            'name': "myfirstmeeting",
            'admin': {'login': 'sergey'}
        }
        response = self.client.post('/meetings/', data=data, format='json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['admin'], 'sergey')
        self.assertEqual(content['start_time'], '2122-09-27T10:11:00')

    def test_list(self):
        response = self.client.get('/meetings/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content[0]['meeting_id'], 'id1')
        self.assertEqual(content[1]['meeting_id'], 'id2')
        self.assertEqual(content[2]['meeting_id'], 'id3')

    def test_no_start(self):
        data = {
            'name': "myfirstmeeting",
            'admin': {'login': 'sergey'}
        }
        response = self.client.post('/meetings/', data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_incorrect_time(self):
        data = {
            'start_time': '10:11:00 2123.09.27',
            'end_time': '10:11:00 2123.09.27',
            'name': "myfirstmeeting",
            'admin': {'login': 'sergey'}
        }
        response = self.client.post('/meetings/', data=data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'meeting should begins earlier than ends')

        data.update({
            'start_time': '10:11:00 2022.09.27',
            'end_time': '10:15:00 2022.09.27'
        })
        response = self.client.post('/meetings/', data=data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'meeting can\'t be created in this time')
