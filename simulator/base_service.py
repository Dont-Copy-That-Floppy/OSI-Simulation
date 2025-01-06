class BaseService:
    def __init__(self, name, port):
        self.name = name
        self.port = port

    def process_request(self, data):
        """
        Override this method in derived classes to handle specific protocol logic.
        """
        raise NotImplementedError("This method must be implemented by subclasses.")
