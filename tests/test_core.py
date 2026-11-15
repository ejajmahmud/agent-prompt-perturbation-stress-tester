"""Automated test suite for Prompt Perturbation Stress Tester."""
import unittest
from agent_prompt_perturbation_stress_tester.core import PromptPerturbationTester

class TestPromptPerturbationTester(unittest.TestCase):
    def test_suite_generation(self):
        suite = PromptPerturbationTester.generate_suite("bypass test")
        self.assertGreater(len(suite), 3)
        self.assertTrue(any("4" in s or "3" in s for s in suite))
