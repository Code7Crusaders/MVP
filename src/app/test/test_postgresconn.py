import unittest
from unittest.mock import patch, MagicMock
from src.app.dependencies.dependency_inj import initialize_postgres
import psycopg2

class TestPostgresConnection(unittest.TestCase):
    @patch('app.dependencies.dependency_inj.psycopg2.connect')
    def test_initialize_postgres(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        
        postgres_adapter = initialize_postgres()
        
        self.assertIsNotNone(postgres_adapter)
        mock_connect.assert_called_once()
    
    @patch('app.dependencies.dependency_inj.psycopg2.connect')
    def test_connection_successful(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        
        try:
            initialize_postgres()
            connection_successful = True
        except Exception:
            connection_successful = False
        
        self.assertTrue(connection_successful)
        mock_connect.assert_called_once()

if __name__ == '__main__':
    unittest.main()
