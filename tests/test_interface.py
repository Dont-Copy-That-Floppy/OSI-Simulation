import unittest
from interface.cli_interface import CLIInterface

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLIInterface()

    def test_add_device(self):
        self.cli.manager.add_device({"name": "Device1", "mac_address": "00:1B:44:11:3A:B7"})
        specs = self.cli.manager.get_layer_specs("Physical")
        self.assertIn("Device1", specs["devices"])

if __name__ == "__main__":
    unittest.main()
