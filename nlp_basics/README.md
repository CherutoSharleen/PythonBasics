# Tokenization Lab

This mini lab provides simple text normalization, tokenization, and unique-term extraction utilities.

## Run

```bash
cd nlp_basics
python -c "from token_lab import tokens, unique_terms; print(tokens('Search ranking and Python')); print(unique_terms('python python ranking'))"
```

## Test

```bash
cd nlp_basics
python -m unittest test_token_lab.py
```
