class Device:
    def __init__(self, name, service_manager):
        self.name = name
        self.service_manager = service_manager

    def send_data(self, port, data):
        service = self.service_manager.get_service(port)
        if not service:
            print(f"No service found on port {port}.")
            return
        response = service.process_request(data)
        print(f"{self.name} received: {response}")

    def receive_signal(self, data):
        print(f"{self.name} received signal: {data}")
