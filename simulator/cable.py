import random

class Cable:
    CABLE_TYPES = {
        "Cat5": {"speed": 100, "bandwidth": "100 Mbps", "error_rate": 0.02, "interfaces": ["RJ45"]},
        "Cat6": {"speed": 1000, "bandwidth": "1 Gbps", "error_rate": 0.01, "interfaces": ["RJ45"]},
        "Fiber Optic": {"speed": 10000, "bandwidth": "10+ Gbps", "error_rate": 0.001, "interfaces": ["LC", "SC"]},
        "WiFi 802.11ac": {"speed": 1300, "bandwidth": "1.3 Gbps", "error_rate": 0.03, "interfaces": ["WiFi"]},
    }

    def __init__(self, cable_type="Cat5"):
        if cable_type not in self.CABLE_TYPES:
            raise ValueError(f"Unsupported cable type: {cable_type}")
        specs = self.CABLE_TYPES[cable_type]
        self.cable_type = cable_type
        self.speed = specs["speed"]
        self.bandwidth = specs["bandwidth"]
        self.error_rate = specs["error_rate"]
        self.interfaces = specs["interfaces"]
        self.connected_interfaces = []
        self.visualizer = None

    def connect_interface(self, interface):
        if interface.interface_type not in self.interfaces:
            print(f"Error: {interface.interface_type} is not compatible with {self.cable_type} cable.")
            return
        if interface not in self.connected_interfaces:
            self.connected_interfaces.append(interface)
            print(f"Interface {interface.name} connected to {self.cable_type} cable.")
            if self.visualizer:
                self.visualizer(f"Interface {interface.name} connected to {self.cable_type} cable.")

    def disconnect_interface(self, interface):
        if interface in self.connected_interfaces:
            self.connected_interfaces.remove(interface)
            print(f"Interface {interface.name} disconnected from {self.cable_type} cable.")
            if self.visualizer:
                self.visualizer(f"Interface {interface.name} disconnected from {self.cable_type} cable.")

    def simulate_error(self, data):
        if random.random() < self.error_rate:
            corrupted_data = "".join(random.choice("01") for _ in data)
            print(f"Error introduced on {self.cable_type}: {corrupted_data}")
            if self.visualizer:
                self.visualizer(f"Error introduced on {self.cable_type}: {corrupted_data}")
            return corrupted_data
        return data

    def transmit_signal(self, data):
        print(f"Transmitting data: {data} at {self.speed} Mbps over {self.cable_type} cable")
        if self.visualizer:
            self.visualizer(f"Transmitting data: {data} at {self.speed} Mbps over {self.cable_type} cable")
        transmitted_data = self.simulate_error(data)
        for interface in self.connected_interfaces:
            interface.receive_signal(transmitted_data)
