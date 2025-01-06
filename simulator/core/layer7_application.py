import http.server
import socketserver
import threading
from base_service import BaseService
from simulator.base_layer import BaseLayer


class ApplicationLayer(BaseLayer):
    def __init__(self):
        super().__init__("Application")
        self.connected_layer6 = None
        self.services = {}  # {protocol: service_handler}

    def connect_to_presentation_layer(self, layer6):
        self.connected_layer6 = layer6

    def register_service(self, protocol, handler):
        """
        Register a service handler for a protocol (e.g., HTTP, FTP).
        """
        self.services[protocol] = handler
        print(f"Application Layer: Registered service for protocol {protocol}")

    def send_request(self, protocol, data, session_id=None):
        """
        Simulate a request to a service.
        """
        if protocol not in self.services:
            print(f"Application Layer: Protocol {protocol} not supported.")
            return

        print(f"Application Layer: Sending {protocol} request: {data}")
        processed_data = self.services[protocol].handle_request(data)

        # Pass processed data to the Presentation Layer
        if self.connected_layer6 and session_id:
            self.connected_layer6.process_data(processed_data, operation="encode", session_id=session_id)
        else:
            print("Error: No presentation layer connected!")

    def receive_response(self, protocol, response):
        """
        Simulate receiving a response from a service.
        """
        if protocol not in self.services:
            print(f"Application Layer: Protocol {protocol} not supported.")
            return

        print(f"Application Layer: Received {protocol} response: {response}")


class HTTPServerApp:
    def __init__(self, port=8080):
        self.port = port
        self.server_thread = None

    def start_server(self):
        handler = http.server.SimpleHTTPRequestHandler
        self.server = socketserver.TCPServer(("0.0.0.0", self.port), handler)
        print(f"HTTP server running on port {self.port}.")

        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

    def stop_server(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            print("HTTP server stopped.")


class HTTPClientApp:
    def send_request(self, server_ip, port, path="/"):
        import requests

        url = f"http://{server_ip}:{port}{path}"
        print(f"HTTP Client sending request to {url}")
        response = requests.get(url)
        print(f"Response: {response.status_code} - {response.text}")
        return response


class AttachableService:
    def __init__(self, name, port):
        self.name = name
        self.port = port

    def process_request(self, data):
        print(f"Processing request on {self.name}: {data}")
        return f"Response from {self.name}"


class HTTPServerApp(AttachableService):
    def __init__(self, port=8080):
        super().__init__("HTTP Server", port)
        self.server_thread = None

    def process_request(self, data):
        print(f"HTTP Server received: {data}")
        return f"HTTP Response: {data}"

    # Realistic server behavior can be added as needed


class HTTPService(BaseService):
    def __init__(self, port=8080):
        super().__init__("HTTP Service", port)

    def process_request(self, data):
        print(f"HTTP Service processing request: {data}")
        return f"HTTP Response: {data}"


class FTPService(BaseService):
    def __init__(self, port=21):
        super().__init__("FTP Service", port)

    def process_request(self, data):
        print(f"FTP Service processing request: {data}")
        return f"FTP Response: {data}"


class DNSService(BaseService):
    def __init__(self, port=53):
        super().__init__("DNS Service", port)

    def process_request(self, data):
        print(f"DNS Service resolving query: {data}")
        return f"Resolved IP for {data}: 192.168.1.100"
