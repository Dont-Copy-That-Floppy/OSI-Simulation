import sys
from PyQt5.QtWidgets import QApplication
from simulator.gui import NetworkSimulatorApp

def main():
    app = QApplication(sys.argv)
    simulator_app = NetworkSimulatorApp()
    simulator_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
