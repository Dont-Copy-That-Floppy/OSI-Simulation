from core.base_layer import BaseLayer
import base64
import zlib

class PresentationLayer(BaseLayer):
    def __init__(self):
        super().__init__("Presentation")
        self.connected_layer5 = None

    def connect_to_session_layer(self, layer5):
        self.connected_layer5 = layer5

    def encode(self, data):
        """
        Encode data using Base64.
        """
        encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        print(f"Presentation Layer: Encoding data: {data} -> {encoded_data}")
        return encoded_data

    def decode(self, encoded_data):
        """
        Decode Base64-encoded data.
        """
        decoded_data = base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')
        print(f"Presentation Layer: Decoding data: {encoded_data} -> {decoded_data}")
        return decoded_data

    def compress(self, data):
        """
        Compress data using zlib.
        """
        compressed_data = zlib.compress(data.encode('utf-8'))
        print(f"Presentation Layer: Compressing data: {data} -> {compressed_data}")
        return compressed_data

    def decompress(self, compressed_data):
        """
        Decompress zlib-compressed data.
        """
        decompressed_data = zlib.decompress(compressed_data).decode('utf-8')
        print(f"Presentation Layer: Decompressing data: {compressed_data} -> {decompressed_data}")
        return decompressed_data

    def encrypt(self, data, key="secret"):
        """
        Simple XOR-based encryption for demonstration purposes.
        """
        encrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
        print(f"Presentation Layer: Encrypting data: {data} -> {encrypted}")
        return encrypted

    def decrypt(self, encrypted_data, key="secret"):
        """
        Simple XOR-based decryption for demonstration purposes.
        """
        decrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(encrypted_data))
        print(f"Presentation Layer: Decrypting data: {encrypted_data} -> {decrypted}")
        return decrypted

    def process_data(self, data, operation, session_id=None):
        """
        Process data for encoding, decoding, compression, decompression, encryption, or decryption.
        """
        result = None
        if operation == "encode":
            result = self.encode(data)
        elif operation == "decode":
            result = self.decode(data)
        elif operation == "compress":
            result = self.compress(data)
        elif operation == "decompress":
            result = self.decompress(data)
        elif operation == "encrypt":
            result = self.encrypt(data)
        elif operation == "decrypt":
            result = self.decrypt(data)
        else:
            print(f"Presentation Layer: Unsupported operation '{operation}'.")

        # Pass to the Session Layer
        if self.connected_layer5 and session_id:
            self.connected_layer5.process_data(result, session_id=session_id, dest_ip=None)
        return result
