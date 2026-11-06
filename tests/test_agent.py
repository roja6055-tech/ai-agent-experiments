import unittest

from src.agent import run_agent


class AgentTests(unittest.TestCase):
    def test_addition_tool(self):
        self.assertIn("The sum is 42.", run_agent("Add 18 and 24"))

    def test_project_note_tool(self):
        self.assertIn(
            "in progress",
            run_agent("What is the status of the sample model review?"),
        )

    def test_unknown_request_does_not_execute_tool(self):
        self.assertIn("couldn't map", run_agent("Tell me a joke"))


if __name__ == "__main__":
    unittest.main()
