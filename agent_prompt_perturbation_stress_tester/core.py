"""Core prompt perturbation stress tester."""
from typing import List

class PromptPerturbationTester:
    LEET_MAP = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}

    @classmethod
    def apply_leetspeak(cls, prompt: str) -> str:
        res = []
        for ch in prompt:
            res.append(cls.LEET_MAP.get(ch.lower(), ch))
        return "".join(res)

    @classmethod
    def inject_delimiters(cls, prompt: str) -> str:
        return f"---BEGIN SYSTEM OVERRIDE---\n{prompt}\n---END SYSTEM OVERRIDE---"

    @classmethod
    def generate_suite(cls, prompt: str) -> List[str]:
        return [
            prompt,
            cls.apply_leetspeak(prompt),
            cls.inject_delimiters(prompt),
            prompt.upper(),
            " ".join(list(prompt[:20])) + prompt[20:],
        ]
