import unittest
from manager.simulation_manager import SimulationManager
from core.cable import Cable
from devices.nic import NIC
import json
from tests.custom_test_result import CustomTestResult


class CLIInterface:
    def __init__(self):
        self.manager = SimulationManager()

    def run(self):
        print("Welcome to the OSI Layer Network Simulator (CLI)")
        while True:
            print("\nOptions:")
            print("1. Add Cable")
            print("2. Add Device")
            print("3. View Layer Specs")
            print("4. Run Tests")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.add_cable()
            elif choice == "2":
                self.add_device()
            elif choice == "3":
                self.view_layer_specs()
            elif choice == "4":
                self.run_tests()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

    def add_cable(self):
        cable_type = input("Enter cable type (e.g., Cat6): ")
        cable = Cable(cable_type)
        self.manager.add_cable(cable)
        print(f"Added cable: {cable.cable_type}")

    def add_device(self):
        name = input("Enter device name: ")
        mac_address = input("Enter MAC address: ")
        device = NIC(name, mac_address)
        self.manager.add_device(device)
        print(f"Added device: {device.name} with MAC address {mac_address}")

    def view_layer_specs(self):
        layer_name = input("Enter layer name (e.g., Physical): ")
        specs = self.manager.get_layer_specs(layer_name)
        if specs:
            print(f"\n{layer_name} Layer Specs:")
            for key, value in specs.items():
                print(f"{key}: {', '.join(value)}")
        else:
            print(f"Layer '{layer_name}' not found.")

    def run_tests(self):
        """
        Run all tests and generate a structured report.
        """
        print("Running all tests...\n")

        # Run tests and capture results
        loader = unittest.TestLoader()
        suite = loader.discover("tests")
        runner = unittest.TextTestRunner(verbosity=2, resultclass=CustomTestResult)

        result = runner.run(suite)

        # Generate a structured report
        report = {
            "total_tests": result.testsRun,
            "failures": [{"test": str(f[0]), "details": str(f[1])} for f in result.failures],
            "errors": [{"test": str(e[0]), "details": str(e[1])} for e in result.errors],
            "skipped": [{"test": str(s[0]), "details": str(s[1])} for s in result.skipped],
            "successes": [str(test) for test in result.successes],
        }

        # Write report to a file
        with open("test_report.json", "w") as report_file:
            json.dump(report, report_file, indent=4)

        print("\nTest Report Summary:")
        print(f"Total Tests: {report['total_tests']}")
        print(f"Passed: {len(report['successes'])}")
        print(f"Failures: {len(report['failures'])}")
        print(f"Errors: {len(report['errors'])}")
        print(f"Skipped: {len(report['skipped'])}")

        print("\nDetailed report written to 'test_report.json'.")


if __name__ == "__main__":
    cli = CLIInterface()
    cli.run()
