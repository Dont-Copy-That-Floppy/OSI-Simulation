class ServiceManager:
    def __init__(self):
        self.services = {}  # {port: service}

    def register_service(self, service):
        if service.port in self.services:
            raise ValueError(f"Port {service.port} is already in use by {self.services[service.port].name}.")
        self.services[service.port] = service
        print(f"Service '{service.name}' registered on port {service.port}.")

    def unregister_service(self, port):
        if port not in self.services:
            raise ValueError(f"Port {port} is not in use.")
        removed_service = self.services.pop(port)
        print(f"Service '{removed_service.name}' unregistered from port {port}.")

    def get_service(self, port):
        return self.services.get(port, None)

    def list_services(self):
        return {port: service.name for port, service in self.services.items()}
