from __future__ import annotations

import re


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", normalize(text))


def unique_terms(text: str) -> list[str]:
    return sorted(set(tokens(text)))
