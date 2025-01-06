from core.layer1_physical import PhysicalLayer

class SimulationManager:
    def __init__(self):
        self.physical_layer = PhysicalLayer()
        # Initialize other layers here...

    def add_device(self, device):
        self.physical_layer.add_device(device)

    def add_cable(self, cable):
        self.physical_layer.add_cable(cable)

    def get_layer_specs(self, layer_name):
        if layer_name == "Physical":
            return self.physical_layer.get_specs()
        # Add handling for other layers...
        return None
