class HardwareInterface:
    def __init__(self, name, interface_type="RJ45"):
        self.name = name
        self.interface_type = interface_type
        self.connected_cable = None

    def connect_to_cable(self, cable):
        if self.connected_cable:
            print(f"{self.name} is already connected to a cable. Disconnect first.")
            return
        if self.interface_type not in cable.interfaces:
            print(f"Error: {self.interface_type} is not compatible with {cable.cable_type} cable.")
            return
        cable.connect_interface(self)
        self.connected_cable = cable
        print(f"{self.name} connected to {cable.cable_type} cable.")

    def disconnect_from_cable(self):
        if not self.connected_cable:
            print(f"{self.name} is not connected to any cable.")
            return
        self.connected_cable.disconnect_interface(self)
        print(f"{self.name} disconnected from {self.connected_cable.cable_type} cable.")
        self.connected_cable = None

    def receive_signal(self, data):
        print(f"{self.name} received signal: {data}")
