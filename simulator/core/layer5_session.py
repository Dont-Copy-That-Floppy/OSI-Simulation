from simulator.base_layer import BaseLayer

class SessionLayer(BaseLayer):
    def __init__(self):
        super().__init__("Session")
        self.sessions = {}  # {session_id: {"state": "active", "data": []}}
        self.connected_layer4 = None

    def connect_to_transport_layer(self, layer4):
        self.connected_layer4 = layer4

    def create_session(self, session_id):
        """
        Establish a new session.
        """
        if session_id in self.sessions:
            print(f"Session Layer: Session {session_id} already exists.")
            return
        self.sessions[session_id] = {"state": "active", "data": []}
        print(f"Session Layer: Session {session_id} established.")

    def terminate_session(self, session_id):
        """
        Terminate an existing session.
        """
        if session_id not in self.sessions:
            print(f"Session Layer: Session {session_id} does not exist.")
            return
        self.sessions[session_id]["state"] = "terminated"
        print(f"Session Layer: Session {session_id} terminated.")

    def process_data(self, data, session_id, dest_ip, source_port=5000, dest_port=80):
        """
        Send data as part of a session.
        """
        if session_id not in self.sessions or self.sessions[session_id]["state"] != "active":
            print(f"Session Layer: No active session {session_id}. Cannot send data.")
            return

        print(f"Session Layer: Sending data through session {session_id}")
        self.sessions[session_id]["data"].append(data)

        # Send data to the Transport Layer
        if self.connected_layer4:
            self.connected_layer4.process_data(data, dest_ip, source_port, dest_port)
        else:
            print("Error: No transport layer connected!")

    def receive_data(self, data, session_id):
        """
        Receive data as part of a session.
        """
        if session_id not in self.sessions or self.sessions[session_id]["state"] != "active":
            print(f"Session Layer: No active session {session_id}. Cannot receive data.")
            return

        print(f"Session Layer: Receiving data through session {session_id}")
        self.sessions[session_id]["data"].append(data)
