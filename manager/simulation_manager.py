from core.layer1_physical import PhysicalLayer
from core.layer2_datalink import DataLinkLayer
from core.layer3_network import NetworkLayer
from core.layer4_transport import TransportLayer
from core.layer5_session import SessionLayer
from core.layer6_presentation import PresentationLayer
from core.layer7_application import ApplicationLayer
from devices.nic import NIC
from core.cable import Cable


class SimulationManager:
    def __init__(self):
        # Create a default physical interface
        self.physical_layer = PhysicalLayer(name="Default Physical Interface", interface_type="RJ45")
        self.datalink_layer = DataLinkLayer()
        self.network_layer = NetworkLayer()
        self.transport_layer = TransportLayer()
        self.session_layer = SessionLayer()
        self.presentation_layer = PresentationLayer()
        self.application_layer = ApplicationLayer()

        self.devices = []
        self.cables = []

    def add_device(self, device):
        """
        Add a device to the simulation, associating it with the Physical Layer.
        """
        if not isinstance(device, NIC):
            raise ValueError("Only NIC devices are supported in the Physical Layer.")

        self.physical_layer.add_device(device)
        self.devices.append(device)
        print(f"Device '{device.name}' added with MAC address '{device.mac_address}'.")

    def add_cable(self, cable):
        """
        Add a cable to the simulation, associating it with the Physical Layer.
        """
        if not isinstance(cable, Cable):
            raise ValueError("Invalid cable type.")

        self.physical_layer.add_cable(cable)
        self.cables.append(cable)
        print(f"Cable '{cable.cable_type}' added to the simulation.")

    def connect_device_to_cable(self, device_name, cable_index):
        """
        Connect a device to a specific cable.
        """
        device = next((d for d in self.devices if d.name == device_name), None)
        if not device:
            raise ValueError(f"Device '{device_name}' not found.")

        if cable_index < 0 or cable_index >= len(self.cables):
            raise IndexError(f"Cable index '{cable_index}' is out of bounds.")

        cable = self.cables[cable_index]
        cable.connect_device(device)
        print(f"Device '{device.name}' connected to Cable '{cable.cable_type}'.")

    def get_layer_specs(self, layer_name):
        """
        Retrieve the specifications for a specific OSI layer.
        """
        layers = {
            "Physical": self.physical_layer,
            "Data Link": self.datalink_layer,
            "Network": self.network_layer,
            "Transport": self.transport_layer,
            "Session": self.session_layer,
            "Presentation": self.presentation_layer,
            "Application": self.application_layer,
        }

        layer = layers.get(layer_name)
        if not layer:
            return None
        return layer.get_specs()

    def transmit_data(self, data, source_device_name, dest_device_name):
        """
        Simulate data transmission from one device to another through the OSI stack.
        """
        source_device = next((d for d in self.devices if d.name == source_device_name), None)
        dest_device = next((d for d in self.devices if d.name == dest_device_name), None)

        if not source_device or not dest_device:
            raise ValueError(f"Source or destination device not found.")

        print(f"Transmitting data from '{source_device.name}' to '{dest_device.name}': {data}")
        self.application_layer.process_data(data, source_device, dest_device)

    def reset_simulation(self):
        """
        Reset the simulation by clearing all layers, devices, and cables.
        """
        self.physical_layer = PhysicalLayer()
        self.datalink_layer = DataLinkLayer()
        self.network_layer = NetworkLayer()
        self.transport_layer = TransportLayer()
        self.session_layer = SessionLayer()
        self.presentation_layer = PresentationLayer()
        self.application_layer = ApplicationLayer()

        self.devices.clear()
        self.cables.clear()
        print("Simulation reset to initial state.")
