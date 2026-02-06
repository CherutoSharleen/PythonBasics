import unittest

from token_lab import tokens, unique_terms


class TokenLabTests(unittest.TestCase):
    def test_tokenization(self) -> None:
        self.assertEqual(tokens("Search, ranking and Python!"), ["search", "ranking", "and", "python"])

    def test_unique_terms(self) -> None:
        self.assertEqual(unique_terms("python python ranking"), ["python", "ranking"])


if __name__ == "__main__":
    unittest.main()
