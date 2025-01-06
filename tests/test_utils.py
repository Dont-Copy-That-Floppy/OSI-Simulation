import unittest
from utils.utils import generate_mac

class TestUtils(unittest.TestCase):
    def test_generate_mac(self):
        mac = generate_mac()
        self.assertTrue(isinstance(mac, str))
        self.assertEqual(len(mac.split(":")), 6)

if __name__ == "__main__":
    unittest.main()
