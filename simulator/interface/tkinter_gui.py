import tkinter as tk
from tkinter import ttk
from manager.simulation_manager import SimulationManager
from simulator.cable import Cable
from core.layer1_physical import HardwareInterface

class OSILayerSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("OSI Layer Network Simulator")
        self.root.geometry("1000x700")

        # Initialize Simulation Manager
        self.manager = SimulationManager()

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        self.control_frame = ttk.Frame(self.root, width=200)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.visualization_frame = ttk.Frame(self.root)
        self.visualization_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add Control Buttons
        self.add_controls()

        # Visualization Canvas
        self.visualization_canvas = tk.Canvas(self.visualization_frame, bg="white")
        self.visualization_canvas.pack(fill=tk.BOTH, expand=True)

    def add_controls(self):
        ttk.Label(self.control_frame, text="Controls", font=("Arial", 14)).pack(pady=10)

        # Add Cable Button
        self.add_cable_button = ttk.Button(self.control_frame, text="Add Cable", command=self.add_cable)
        self.add_cable_button.pack(pady=5)

        # Add Device Button
        self.add_device_button = ttk.Button(self.control_frame, text="Add Device", command=self.add_device)
        self.add_device_button.pack(pady=5)

        # Refresh Visualization
        self.refresh_button = ttk.Button(self.control_frame, text="Refresh", command=self.update_visualization)
        self.refresh_button.pack(pady=5)

    def add_cable(self):
        cable = Cable("Cat6")
        self.manager.add_cable(cable)
        self.update_visualization()

    def add_device(self):
        device = HardwareInterface(f"Device{len(self.manager.physical_layer.devices) + 1}", "RJ45")
        self.manager.add_device(device)
        self.update_visualization()

    def update_visualization(self):
        self.visualization_canvas.delete("all")
        specs = self.manager.get_layer_specs("Physical")

        y_position = 20
        for i, cable in enumerate(specs["cables"]):
            self.visualization_canvas.create_text(10, y_position, anchor=tk.W, text=f"Cable {i + 1}: {cable}")
            y_position += 20

        for i, device in enumerate(specs["devices"]):
            self.visualization_canvas.create_text(10, y_position, anchor=tk.W, text=f"Device {i + 1}: {device}")
            y_position += 20


if __name__ == "__main__":
    root = tk.Tk()
    app = OSILayerSimulator(root)
    root.mainloop()
