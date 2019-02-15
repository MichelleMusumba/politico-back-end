import json
from unittest import TestCase
from run import app, office_list


class OfficeTest(TestCase):
    def setUp(self):
        # Setup a Client
        self.client = app.test_client()

    def tearDown(self):
        office_list.clear()

    def test_view_all_offices_empty(self):
        response = self.client.get('/offices')
        # Check status code
        self.assertEqual(response.status_code, 200)
        # Check if offices exist
        self.assertEqual(response.json['offices'], [])

    def test_view_all_offices(self):
        self.client.post('/offices', data=json.dumps({
            "name": "office_name",
            "type": "office_type"
        }))
        response = self.client.get('/offices')
        self.assertEqual(response.json['offices'][0]['name'], 'office_name')

    def test_view_a_specific_office_fail(self):
        response = self.client.get('/offices/1')
        # Check status code
        self.assertEqual(response.status_code, 400)

    def test_view_a_specific_office_success(self):
        self.client.post('/offices', data=json.dumps({
            "name": "office_name",
            "type": "office_type"
        }))

        response = self.client.get('/offices/1')
        self.assertEqual(response.status_code, 200, "Should be successful ,status code 200")

    def test_create_an_office(self):
        response = self.client.post('/offices', data=json.dumps({
            "name": "office_name",
            "type": "office_type"
        }))

        self.assertEqual(len(response.json['data']), 1)
