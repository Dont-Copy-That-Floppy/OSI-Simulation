class BaseDevice:
    def __init__(self, name):
        self.name = name
        self.connected = False  # Tracks connection status

    def connect(self):
        self.connected = True
        print(f"{self.name} connected.")

    def disconnect(self):
        self.connected = False
        print(f"{self.name} disconnected.")

    def get_specs(self):
        """
        Return basic device specifications.
        """
        return {"name": self.name, "connected": self.connected}
