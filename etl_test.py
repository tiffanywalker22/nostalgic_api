import unittest
from unittest.mock import patch, MagicMock
import etl
import psycopg2

class TestETL(unittest.TestCase):

    @patch('etl.psycopg2.connect')
    def test_connect_db(self, mock_connect):
        mock_connect.return_value = MagicMock()
        conn = etl.connect_db(etl.db_config)
        mock_connect.assert_called_with(**etl.db_config)
        self.assertIsNotNone(conn)

if __name__ == '__main__':
    unittest.main()