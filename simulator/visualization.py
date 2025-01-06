import tkinter as tk
from tkinter import ttk
from simulator.layer7_application import ApplicationLayer
from simulator.layer6_presentation import PresentationLayer
from simulator.layer5_session import SessionLayer
from simulator.layer4_transport import TransportLayer
from simulator.layer3_network import NetworkLayer
from simulator.layer2_datalink import DataLinkLayer
from simulator.layer1_physical import PhysicalLayer, HardwareInterface
from simulator.cable import Cable


class OSILayerSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("OSI Layer Network Simulator")
        self.root.geometry("1000x700")

        # OSI Layers
        self.physical_layer = PhysicalLayer()
        self.datalink_layer = None
        self.network_layer = None
        self.transport_layer = None
        self.session_layer = None
        self.presentation_layer = None
        self.application_layer = None

        # Devices and Cables
        self.devices = []
        self.cables = []

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Frames for layout
        self.control_frame = ttk.Frame(self.root, width=200)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.visualization_frame = ttk.Frame(self.root)
        self.visualization_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Control Panel
        self.add_controls()

        # Visualization Area
        self.visualization_canvas = tk.Canvas(self.visualization_frame, bg="white")
        self.visualization_canvas.pack(fill=tk.BOTH, expand=True)

    def add_controls(self):
        ttk.Label(self.control_frame, text="Controls", font=("Arial", 14)).pack(pady=10)

        # Add Cable
        self.add_cable_button = ttk.Button(self.control_frame, text="Add Cable", command=self.add_cable)
        self.add_cable_button.pack(pady=5)

        # Add Device
        self.add_device_button = ttk.Button(self.control_frame, text="Add Device", command=self.add_device)
        self.add_device_button.pack(pady=5)

        # Play Button
        self.play_button = ttk.Button(self.control_frame, text="Play", command=self.play_simulation)
        self.play_button.pack(pady=5)

        # Pause Button
        self.pause_button = ttk.Button(self.control_frame, text="Pause", command=self.pause_simulation)
        self.pause_button.pack(pady=5)

    def add_cable(self):
        """
        Adds a new cable to the simulation.
        """
        cable = Cable("Cat6")
        self.cables.append(cable)
        self.update_visualization()
        print(f"Added cable: {cable.cable_type}")

    def add_device(self):
        """
        Adds a new device to the simulation and connects it to the first cable.
        """
        device = HardwareInterface(f"Device{len(self.devices) + 1}", "RJ45")
        self.devices.append(device)

        # Connect device to the first available cable
        if self.cables:
            self.cables[0].connect_interface(device)
            self.physical_layer.add_interface(device)
            print(f"Added device: {device.name} and connected to cable {self.cables[0].cable_type}")
        else:
            print("No cables available to connect the device.")

        self.update_visualization()

    def play_simulation(self):
        """
        Start the simulation.
        """
        print("Simulation started.")
        # Logic for simulation playback (e.g., data transmission visualization)

    def pause_simulation(self):
        """
        Pause the simulation.
        """
        print("Simulation paused.")
        # Logic for pausing the simulation

    def update_visualization(self):
        """
        Updates the visualization area with the current simulation state.
        """
        self.visualization_canvas.delete("all")
        y_position = 20

        # Draw Cables
        for i, cable in enumerate(self.cables):
            self.visualization_canvas.create_text(10, y_position, anchor=tk.W, text=f"Cable {i + 1}: {cable.cable_type}")
            y_position += 20

        # Draw Devices
        for i, device in enumerate(self.devices):
            self.visualization_canvas.create_text(10, y_position, anchor=tk.W, text=f"Device {i + 1}: {device.name}")
            y_position += 20


if __name__ == "__main__":
    root = tk.Tk()
    app = OSILayerSimulator(root)
    root.mainloop()
