import tkinter as tk
from tkinter import ttk
from manager.simulation_manager import SimulationManager
from core.cable import Cable
from devices.nic import NIC

class OSILayerSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("OSI Layer Network Simulator")
        self.root.geometry("1000x700")

        # Initialize Simulation Manager
        self.manager = SimulationManager()

        # UI Components
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the main UI layout with control and visualization frames.
        """
        # Control Frame (Left Panel)
        self.control_frame = ttk.Frame(self.root, width=200)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Visualization Frame (Right Panel)
        self.visualization_frame = ttk.Frame(self.root)
        self.visualization_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Control Panel Buttons and Inputs
        self.add_controls()

        # Visualization Canvas
        self.visualization_canvas = tk.Canvas(self.visualization_frame, bg="white")
        self.visualization_canvas.pack(fill=tk.BOTH, expand=True)

    def add_controls(self):
        """
        Add buttons and other controls to the control panel.
        """
        ttk.Label(self.control_frame, text="Controls", font=("Arial", 14)).pack(pady=10)

        # Add Cable Button
        self.add_cable_button = ttk.Button(self.control_frame, text="Add Cable", command=self.add_cable)
        self.add_cable_button.pack(pady=5)

        # Add Device Button
        self.add_device_button = ttk.Button(self.control_frame, text="Add Device", command=self.add_device)
        self.add_device_button.pack(pady=5)

        # Select Layer to View
        self.layer_selection = ttk.Combobox(self.control_frame, values=[
            "Physical", "Data Link", "Network", "Transport", "Session", "Presentation", "Application"
        ], state="readonly")
        self.layer_selection.set("Physical")
        self.layer_selection.pack(pady=5)

        # Refresh Visualization Button
        self.refresh_button = ttk.Button(self.control_frame, text="Refresh", command=self.update_visualization)
        self.refresh_button.pack(pady=5)

    def add_cable(self):
        """
        Adds a new cable to the simulation.
        """
        cable_type = "Cat6"  # Hardcoded for now; can be made dynamic.
        cable = Cable(cable_type)
        self.manager.add_cable(cable)
        print(f"Added cable: {cable.cable_type}")
        self.update_visualization()

    def add_device(self):
        """
        Adds a new device to the simulation and connects it to the first available cable.
        """
        device_name = f"Device{len(self.manager.physical_layer.devices) + 1}"
        mac_address = f"00:1B:44:11:3A:{len(self.manager.physical_layer.devices):02X}"
        device = NIC(device_name, mac_address)

        self.manager.add_device(device)
        print(f"Added device: {device.name} with MAC {mac_address}")
        self.update_visualization()

    def update_visualization(self):
        """
        Updates the visualization canvas with the current state of the simulation.
        """
        self.visualization_canvas.delete("all")

        # Get selected layer specs
        selected_layer = self.layer_selection.get()
        specs = self.manager.get_layer_specs(selected_layer)

        if not specs:
            self.visualization_canvas.create_text(
                10, 20, anchor=tk.W, text=f"No data available for {selected_layer} layer."
            )
            return

        # Display layer specs
        y_position = 20
        for key, values in specs.items():
            self.visualization_canvas.create_text(
                10, y_position, anchor=tk.W, text=f"{key}: {', '.join(values)}"
            )
            y_position += 20


if __name__ == "__main__":
    root = tk.Tk()
    app = OSILayerSimulator(root)
    root.mainloop()
