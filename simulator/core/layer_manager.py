class LayerManager:
    def __init__(self):
        self.layers = {}  # {layer_number: layer_instance}

    def register_layer(self, layer_number, layer_instance):
        self.layers[layer_number] = layer_instance

    def send_data(self, from_layer, to_layer, data):
        if from_layer not in self.layers or to_layer not in self.layers:
            raise ValueError(f"Layers {from_layer} or {to_layer} not registered.")
        print(f"Sending data from Layer {from_layer} to Layer {to_layer}: {data}")
        processed_data = self.layers[to_layer].process_data(data)
        return processed_data
