from __future__ import annotations

import re
from collections import Counter


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", normalize(text))


def unique_terms(text: str) -> list[str]:
    return sorted(set(tokens(text)))


def ngrams(text: str, n: int = 2) -> list[tuple[str, ...]]:
    parts = tokens(text)
    if n <= 0:
        raise ValueError("n must be positive")
    return [tuple(parts[i : i + n]) for i in range(0, max(0, len(parts) - n + 1))]


def term_frequency(text: str) -> dict[str, int]:
    return dict(Counter(tokens(text)))


def split_sentences(text: str) -> list[str]:
    raw = re.split(r"(?<=[.!?])\s+", text.strip())
    return [part.strip() for part in raw if part.strip()]
