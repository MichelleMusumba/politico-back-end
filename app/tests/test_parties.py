import json
from unittest import TestCase
from run import app, party_list


class PartyTest(TestCase):
    def setUp(self):
        # Setup a Client
        self.client = app.test_client()

    def tearDown(self):
        party_list.clear()

    def test_view_all_parties_empty(self):
        response = self.client.get('/parties')
        # Check status code
        self.assertEqual(response.status_code, 200)
        # Check if offices exist
        self.assertEqual(response.json['parties'], [])

    def test_view_all_parties_not_empty(self):
        self.client.post('/parties', data=json.dumps({
            "name": "party_name",
            "hqAddress": "party_address",
            "logoUrl": "party_logo"
        }))
        response = self.client.get('/parties')

        self.assertEqual(response.json['parties'][0]['name'], 'party_list')

    def test_view_a_specific_party_fail(self):
        response = self.client.get('/parties/1')
        # Check status code
        self.assertEqual(response.status_code, 404)

    def test_create_a_party(self):
        response = self.client.post('/parties', data=json.dumps({
            "name": "party_name",
            "hqAddress": "party_address",
            "logoUrl": "party_logo"
        }))
        self.assertEqual(response.status_code, 201)

    def test_edit_a_party(self):
        self.client.post('/parties', data=json.dumps({
            "name": "party_name",
            "hqAddress": "party_address",
            "logoUrl": "party_logo"
        }))
        response = self.client.patch('/parties/1/name', data=json.dumps({
            "name": "party_name"
        }))
        self.assertEqual(response.status_code, 200)

    def test_delete_a_party(self):
        self.client.post('/parties', data=json.dumps({
            "name": "party_name",
            "hqAddress": "party_address",
            "logoUrl": "party_logo"
        }))

        resp = self.client.delete('/parties/1')
        self.assertEqual(resp.status_code, 200)
