import unittest

from token_lab import ngrams, term_frequency, tokens, unique_terms


class TokenLabTests(unittest.TestCase):
    def test_tokenization(self) -> None:
        self.assertEqual(tokens("Search, ranking and Python!"), ["search", "ranking", "and", "python"])

    def test_unique_terms(self) -> None:
        self.assertEqual(unique_terms("python python ranking"), ["python", "ranking"])

    def test_bigrams(self) -> None:
        self.assertEqual(ngrams("python ranking model", 2), [("python", "ranking"), ("ranking", "model")])

    def test_term_frequency(self) -> None:
        freq = term_frequency("ranking ranking search")
        self.assertEqual(freq["ranking"], 2)


if __name__ == "__main__":
    unittest.main()
