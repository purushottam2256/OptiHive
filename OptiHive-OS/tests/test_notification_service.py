# services/mobile_notification_service.py
import requests
import logging
from typing import Dict, Any
import unittest
from unittest.mock import patch, Mock
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.mobile_notification_service import send_notification


logger = logging.getLogger(__name__)

def send_notification(device_token: str, title: str, message: str) -> Dict[str, Any]:
    """Send mobile notification with error handling."""
    try:
        url = "YOUR_NOTIFICATION_SERVICE_URL"
        payload = {
            "token": device_token,
            "title": title,
            "message": message
        }
        
        response = requests.post(url, json=payload)
        
        try:
            return response.json()
        except (ValueError, requests.exceptions.JSONDecodeError):
            return {
                "error": "Invalid JSON response",
                "status_code": response.status_code
            }
            
    except requests.RequestException as e:
        return {
            "error": str(e),
            "status_code": getattr(e.response, 'status_code', 500)
        }

# tests/test_notification_service.py


class TestNotificationService(unittest.TestCase):
    
    @patch('services.mobile_notification_service.requests.post')
    def test_send_notification_non_json_response(self, mock_post):
        # Setup mock
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_post.return_value = mock_response

        # Test
        response = send_notification("FAKE_TOKEN", "Test", "Message")
        
        # Assert
        self.assertIsInstance(response, dict)
        self.assertIn("error", response)
        self.assertEqual(response["status_code"], 500)

    @patch('services.mobile_notification_service.requests.post')
    def test_send_notification_success(self, mock_post):
        # Setup mock
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        # Test
        response = send_notification("VALID_TOKEN", "Test", "Message")
        
        # Assert
        self.assertIsInstance(response, dict)
        self.assertIn("success", response)

if __name__ == '__main__':
    unittest.main()