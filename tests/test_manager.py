import unittest
from manager.simulation_manager import SimulationManager
from devices.nic import NIC
from core.cable import Cable

class TestSimulationManager(unittest.TestCase):
    def setUp(self):
        self.manager = SimulationManager()

    def test_add_device(self):
        device = NIC("Device1", "00:1B:44:11:3A:B7")
        self.manager.add_device(device)
        self.assertEqual(len(self.manager.physical_layer.devices), 1)

    def test_add_cable(self):
        cable = Cable("Cat6")
        self.manager.add_cable(cable)
        self.assertEqual(len(self.manager.physical_layer.cables), 1)

    def test_connect_device_to_cable(self):
        device = NIC("Device1", "00:1B:44:11:3A:B7")
        cable = Cable("Cat6")
        self.manager.add_device(device)
        self.manager.add_cable(cable)
        self.manager.connect_device_to_cable("Device1", 0)
        self.assertEqual(cable.connected_devices[0].name, "Device1")

if __name__ == "__main__":
    unittest.main()
