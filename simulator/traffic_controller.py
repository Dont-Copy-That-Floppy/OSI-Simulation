class TrafficController:
    def __init__(self):
        self.running = False
        self.recording = False
        self.logs = []

    def play(self):
        self.running = True
        print("Simulation started.")

    def pause(self):
        self.running = False
        print("Simulation paused.")

    def record(self, log_entry):
        if self.recording:
            self.logs.append(log_entry)
            print(f"Recorded: {log_entry}")

    def toggle_recording(self):
        self.recording = not self.recording
        state = "enabled" if self.recording else "disabled"
        print(f"Recording {state}.")
