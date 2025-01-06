from unittest import TestResult

class CustomTestResult(TestResult):
    """
    Custom TestResult class to capture successful test cases along with failures and errors.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.successes = []

    def addSuccess(self, test):
        """
        Overrides the default addSuccess to capture successful test cases.
        """
        super().addSuccess(test)
        self.successes.append(test)
