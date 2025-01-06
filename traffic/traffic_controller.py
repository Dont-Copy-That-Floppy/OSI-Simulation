class TrafficController:
    def __init__(self):
        self.running = False
        self.paused = False
        self.step_mode = False

    def play(self):
        self.running = True
        self.paused = False
        print("Simulation started.")

    def pause(self):
        if not self.running:
            print("Simulation is not running.")
            return
        self.paused = True
        print("Simulation paused.")

    def step(self):
        if not self.running or self.paused:
            self.step_mode = True
            print("Simulation stepping through.")
        else:
            print("Cannot step while simulation is running.")

    def stop(self):
        self.running = False
        self.paused = False
        print("Simulation stopped.")
