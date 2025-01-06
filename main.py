import sys
from interface.cli_interface import CLIInterface
from interface.gui import OSILayerSimulator
import tkinter as tk

def main():
    print("Welcome to the OSI Layer Network Simulator")
    print("Select an interface:")
    print("1. Graphical User Interface (GUI)")
    print("2. Command-Line Interface (CLI)")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("Launching GUI...")
        root = tk.Tk()
        app = OSILayerSimulator(root)
        root.mainloop()
    elif choice == "2":
        print("Launching CLI...")
        cli = CLIInterface()
        cli.run()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
