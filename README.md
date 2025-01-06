# OSI Layer Network Simulator

## Project Overview
The OSI Layer Network Simulator is a graphical tool designed to simulate physical networks, providing detailed visualization and interaction for each layer of the OSI (Open Systems Interconnection) model. This project aims to facilitate learning, experimentation, and analysis of network behaviors by offering an intuitive platform for network enthusiasts, students, and professionals.

---

## Key Features

- **Layer-by-Layer Simulation:** Visualize and interact with all 7 OSI layers, from the physical layer to the application layer.
- **Custom Network Topologies:** Create, modify, and simulate custom network configurations with various node types, connections, and protocols.
- **Protocol Emulation:** Emulate common networking protocols at each OSI layer (e.g., Ethernet, TCP/IP, HTTP).
- **Traffic Simulation:** Generate and analyze network traffic, including packet flow, latency, and throughput.
- **Error and Recovery Scenarios:** Simulate real-world issues such as packet loss, corruption, and recovery mechanisms.
- **Educational Tools:** Step-through mode to illustrate how data traverses each layer, with detailed annotations and explanations.
- **Statistics and Logging:** Gather performance metrics and logs for further analysis.

---

## OSI Layers Simulated

1. **Physical Layer:**
   - File: `layer1_physical.py`
   - Simulate hardware, cables, and bit-level transmission.
   - Display transmission mediums and signal states.
2. **Data Link Layer:**
   - File: `layer2_datalink.py`
   - Implement MAC addressing and error detection/correction.
   - Visualize frame encapsulation and ARP.
3. **Network Layer:**
   - File: `layer3_network.py`
   - Simulate IP addressing, routing, and packet forwarding.
   - Visualize network layer protocols like IPv4/IPv6.
4. **Transport Layer:**
   - File: `layer4_transport.py`
   - Emulate TCP/UDP operations, port addressing, and reliability mechanisms.
5. **Session Layer:**
   - File: `layer5_session.py`
   - Manage sessions, synchronization, and dialogs.
   - Simulate session states and timeouts.
6. **Presentation Layer:**
   - File: `layer6_presentation.py`
   - Translate data formats, compression, and encryption.
   - Visualize encoding and decoding processes.
7. **Application Layer:**
   - File: `layer7_application.py`
   - Emulate user-level protocols like HTTP, FTP, SMTP.
   - Visualize request-response cycles.

---

## Directory Structure

```plaintext
osi-layer-network-simulator/
├── layer1_physical.py         # Physical layer simulation
├── layer2_datalink.py         # Data link layer simulation
├── layer3_network.py          # Network layer simulation
├── layer4_transport.py        # Transport layer simulation
├── layer5_session.py          # Session layer simulation
├── layer6_presentation.py     # Presentation layer simulation
├── layer7_application.py      # Application layer simulation
├── main.py                    # Entry point for the simulator
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── LICENSE                    # License information
```

---

## TODO

| Task                               | Status      |
|------------------------------------|-------------|
| Implement Physical Layer Logic    | In Progress |
| Add MAC Addressing in Data Link   | Not Started |
| Develop Routing Algorithm         | Not Started |
| Simulate TCP Reliability          | In Progress |
| Session Management Mechanisms     | Not Started |
| Presentation Layer Compression    | Not Started |
| Application Layer Protocols (HTTP)| Not Started |

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/osi-layer-network-git
   cd osi-layer-network-simulator
   ```
2. **Install Dependencies:**
   Ensure you have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Simulator:**
   ```bash
   python main.py
   ```

---

## Usage

1. **Start the Simulator:** Launch the application and select a predefined or custom topology.
2. **Add Network Elements:** Add nodes, links, and configure protocols as needed.
3. **Simulate Traffic:** Generate and observe traffic flow through the network.
4. **Analyze Results:** View performance metrics, logs, and protocol-specific details.

---

## License

This project is licensed under the GPLv3 License. See the LICENSE file for details.

---

## Contact

For questions, suggestions, or feedback, contact:
- **Email:** [@me]
- **GitHub Issues:** [https://github.com/Dont-Copy-That-Floppy/OSI-Simulation]

---


