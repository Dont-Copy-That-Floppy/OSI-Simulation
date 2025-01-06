from devices.base_device import BaseDevice


class NIC(BaseDevice):
    def __init__(self, name, mac_address):
        super().__init__(name)
        self.mac_address = mac_address

    def get_specs(self):
        """
        Return NIC-specific specifications.
        """
        specs = super().get_specs()
        specs["mac_address"] = self.mac_address
        return specs
