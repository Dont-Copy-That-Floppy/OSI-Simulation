from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel

class NetworkSimulatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OSI Layer Network Simulator")
        self.setGeometry(100, 100, 1000, 700)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.play_button = QPushButton("Play")
        self.layout.addWidget(self.play_button)

        self.pause_button = QPushButton("Pause")
        self.layout.addWidget(self.pause_button)

        self.record_button = QPushButton("Record")
        self.layout.addWidget(self.record_button)

        self.visualization_area = QLabel("Traffic Visualization")
        self.layout.addWidget(self.visualization_area)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
