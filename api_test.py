import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
import api

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = api.app.test_client()
        self.app.testing = True

    @patch('api.psycopg2.connect')
    def test_connect_db(self, mock_connect):
        mock_connect.return_value = MagicMock()
        conn = api.connect_db()
        mock_connect.assert_called_with(**api.db_config)
        self.assertIsNotNone(conn)