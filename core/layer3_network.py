from core.base_layer import BaseLayer

class NetworkLayer(BaseLayer):
    def __init__(self, ip_address="192.168.1.1"):
        super().__init__("Network")
        self.ip_address = ip_address
        self.routing_table = {}  # {Destination IP: Next Hop Layer}
        self.connected_layer2 = None

    def connect_to_datalink_layer(self, layer2):
        self.connected_layer2 = layer2

    def add_route(self, destination_ip, next_hop):
        self.routing_table[destination_ip] = next_hop
        print(f"Route added: {destination_ip} -> {next_hop.ip_address}")

    def process_data(self, data, destination_ip=None):
        """
        Create a packet and send it to the Data Link Layer.
        """
        if destination_ip is None:
            print("Error: No destination IP provided.")
            return

        packet = f"Packet(Source={self.ip_address}, Dest={destination_ip}, Data={data})"
        print(f"Network Layer: Encapsulating into {packet}")

        # Determine next hop based on the routing table
        next_hop = self.routing_table.get(destination_ip)
        if not next_hop:
            print(f"Network Layer: No route to {destination_ip}")
            return

        # Send packet to Data Link Layer
        if self.connected_layer2:
            self.connected_layer2.process_data(packet, destination_mac=next_hop.mac_address)
        else:
            print("Error: No data link layer connected!")

    def receive_data(self, packet):
        """
        Process a received packet from the Data Link Layer.
        """
        # Parse the packet
        try:
            parts = packet.strip("Packet()").split(", ")
            packet_dict = {part.split("=")[0]: part.split("=")[1] for part in parts}
        except Exception as e:
            print(f"Error parsing packet: {packet}")
            return

        source_ip = packet_dict.get("Source")
        destination_ip = packet_dict.get("Dest")
        data = packet_dict.get("Data", "")

        # Check if the packet is for this device
        if destination_ip != self.ip_address:
            print(f"Network Layer: Packet ignored, not for this IP ({self.ip_address}).")
            return

        print(f"Network Layer: Successfully received data: {data} from {source_ip}")
