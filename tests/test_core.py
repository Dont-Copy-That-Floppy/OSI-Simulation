import unittest
from core.layer1_physical import PhysicalLayer
from core.cable import Cable

class TestCore(unittest.TestCase):
    def setUp(self):
        self.physical_layer = PhysicalLayer(name="Physical Test Layer")

    def test_add_device(self):
        device = object()  # Mock device
        self.physical_layer.add_device(device)
        self.assertEqual(len(self.physical_layer.devices), 1)

    def test_add_cable(self):
        cable = Cable("Cat6")
        self.physical_layer.add_cable(cable)
        self.assertEqual(len(self.physical_layer.cables), 1)

    def test_get_specs(self):
        cable = Cable("Cat6")
        self.physical_layer.add_cable(cable)
        specs = self.physical_layer.get_specs()
        self.assertIn("Cat6", specs["cables"])

if __name__ == "__main__":
    unittest.main()
