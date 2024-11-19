# tests/test_battery_service.py
import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.battery_status_service import get_battery_status

class TestBatteryService(unittest.TestCase):
    def test_get_battery_status(self):
        result = get_battery_status()
        self.assertIsInstance(result, list)
        if result:
            self.assertIn("name", result[0])
            self.assertIn("status", result[0])
            self.assertIn("estimated_charge_remaining", result[0])

if __name__ == "__main__":
    unittest.main()