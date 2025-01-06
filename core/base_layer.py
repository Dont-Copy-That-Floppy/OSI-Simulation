class BaseLayer:
    def __init__(self, layer_name):
        self.layer_name = layer_name

    def process_data(self, data):
        """
        Override this method to implement layer-specific functionality.
        """
        raise NotImplementedError("process_data must be implemented in subclasses.")
