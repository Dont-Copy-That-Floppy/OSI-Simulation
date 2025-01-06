from core.base_layer import BaseLayer
import random

class TransportLayer(BaseLayer):
    def __init__(self, protocol="TCP"):
        super().__init__("Transport")
        self.protocol = protocol  # "TCP" or "UDP"
        self.connected_layer3 = None
        self.sessions = {}  # {session_id: (source_port, dest_port)}

    def connect_to_network_layer(self, layer3):
        self.connected_layer3 = layer3

    def generate_session_id(self, source_port, dest_port):
        return f"{source_port}-{dest_port}"

    def create_connection(self, source_port, dest_port):
        """
        Simulates a TCP handshake if using TCP.
        """
        session_id = self.generate_session_id(source_port, dest_port)
        if self.protocol == "TCP":
            print(f"Transport Layer: Initiating TCP handshake for session {session_id}")
            print(f"Transport Layer: TCP handshake complete for session {session_id}")
        self.sessions[session_id] = (source_port, dest_port)

    def process_data(self, data, dest_ip, source_port=5000, dest_port=80):
        """
        Segments data and sends it via the Network Layer.
        """
        session_id = self.generate_session_id(source_port, dest_port)
        if self.protocol == "TCP" and session_id not in self.sessions:
            self.create_connection(source_port, dest_port)

        segment = f"Segment(Protocol={self.protocol}, SourcePort={source_port}, DestPort={dest_port}, Data={data})"
        print(f"Transport Layer: Encapsulating into {segment}")

        # Send segment to the Network Layer
        if self.connected_layer3:
            self.connected_layer3.process_data(segment, dest_ip)
        else:
            print("Error: No network layer connected!")

    def receive_data(self, segment):
        """
        Process a received segment from the Network Layer.
        """
        # Parse the segment
        try:
            parts = segment.strip("Segment()").split(", ")
            segment_dict = {part.split("=")[0]: part.split("=")[1] for part in parts}
        except Exception as e:
            print(f"Error parsing segment: {segment}")
            return

        protocol = segment_dict.get("Protocol")
        source_port = int(segment_dict.get("SourcePort", 0))
        dest_port = int(segment_dict.get("DestPort", 0))
