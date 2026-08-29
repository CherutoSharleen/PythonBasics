import unittest

from token_lab import (
    contains_all_terms,
    keyword_positions,
    ngrams,
    split_sentences,
    term_frequency,
    token_count,
    tokens,
    unique_terms,
)


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

    def test_split_sentences(self) -> None:
        parts = split_sentences("Rank documents. Explain scores! Keep examples short?")
        self.assertEqual(len(parts), 3)

    def test_keyword_positions(self) -> None:
        positions = keyword_positions("search rank search explain", "search")
        self.assertEqual(positions, [0, 2])

    def test_contains_all_terms(self) -> None:
        self.assertTrue(contains_all_terms("search ranking pipeline", ["search", "ranking"]))
        self.assertFalse(contains_all_terms("search ranking pipeline", ["search", "python"]))

    def test_token_count(self) -> None:
        self.assertEqual(token_count("search ranking pipeline"), 3)


if __name__ == "__main__":
    unittest.main()
