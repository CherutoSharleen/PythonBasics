import unittest

from token_lab import ngrams, tokens, unique_terms


class TokenLabTests(unittest.TestCase):
    def test_tokenization(self) -> None:
        self.assertEqual(tokens("Search, ranking and Python!"), ["search", "ranking", "and", "python"])

    def test_unique_terms(self) -> None:
        self.assertEqual(unique_terms("python python ranking"), ["python", "ranking"])

    def test_bigrams(self) -> None:
        self.assertEqual(ngrams("python ranking model", 2), [("python", "ranking"), ("ranking", "model")])


if __name__ == "__main__":
    unittest.main()
