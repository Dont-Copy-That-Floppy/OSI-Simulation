from core.base_layer import BaseLayer
import random

class DataLinkLayer(BaseLayer):
    def __init__(self, mac_address="00:1B:44:11:3A:B7"):
        super().__init__("Data Link")
        self.mac_address = mac_address
        self.connected_layer1 = None
        self.connected_peers = {}  # {MAC: DataLinkLayer instance}

    def connect_to_physical_layer(self, layer1):
        self.connected_layer1 = layer1

    def add_peer(self, peer_mac, peer_layer):
        self.connected_peers[peer_mac] = peer_layer

    def generate_crc(self, data):
        """
        Simulate CRC (Cyclic Redundancy Check) for error detection.
        """
        crc = sum(ord(char) for char in data) % 256  # Simplistic CRC simulation
        return crc

    def validate_crc(self, data, crc):
        """
        Validate received CRC.
        """
        return self.generate_crc(data) == crc

    def process_data(self, data, destination_mac=None):
        """
        Create a frame and send it via the Physical Layer.
        """
        crc = self.generate_crc(data)
        frame = f"Frame(Source={self.mac_address}, Dest={destination_mac}, CRC={crc}, Data={data})"
        print(f"Data Link Layer: Encapsulating into {frame}")
        
        # Send frame to Layer 1
        if self.connected_layer1:
            self.connected_layer1.process_data(frame)
        else:
            print("Error: No physical layer connected!")

    def receive_data(self, frame):
        """
        Process received frame from the Physical Layer.
        """
        # Parse the frame (simplistic parsing)
        try:
            parts = frame.strip("Frame()").split(", ")
            frame_dict = {part.split("=")[0]: part.split("=")[1] for part in parts}
        except Exception as e:
            print(f"Error parsing frame: {frame}")
            return

        source_mac = frame_dict.get("Source")
        destination_mac = frame_dict.get("Dest")
        crc = int(frame_dict.get("CRC", 0))
        data = frame_dict.get("Data", "")

        # Validate CRC and destination MAC
        if destination_mac != self.mac_address:
            print(f"Data Link Layer: Frame ignored, not for this MAC ({self.mac_address}).")
            return

        if not self.validate_crc(data, crc):
            print("Data Link Layer: CRC check failed, data corrupted.")
            return

        print(f"Data Link Layer: Successfully received data: {data} from {source_mac}")
