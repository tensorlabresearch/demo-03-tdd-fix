# Demo 03 — TDD Bug Fix

**Concept:** Write the failing test first, then fix the code.

## What this teaches

Test-driven development as a forcing function: writing the test first makes you
define correct behavior precisely before touching production code. This demo shows
how an `AGENTS.md` workflow section can lock an agent into a strict red-green cycle.

The AGENTS.md task workflow:
1. Write a failing test that encodes the exact behavior rule
2. Run it — confirm it fails for the right reason
3. Make the smallest change that passes the test
4. Run the full suite

## The bug

`src/pricing.py` has a `calculate_price(price, discount, tax)` function that applies
operations in the wrong order. The spec says: **apply discount to base price, then
apply tax to the discounted price.**

## The codebase

```
src/pricing.py        — calculate_price function with the bug
tests/test_pricing.py — existing test suite
AGENTS.md             — enforces the TDD workflow
PROMPT.md             — the prompt to give Claude
```

## Running the demo

```bash
pytest tests/ -x --tb=short
```

Then open Claude Code in this directory and paste the prompt from `PROMPT.md`.

## Expected behavior

Claude should write a failing test first, run it, see it fail, then make the minimal
change to `src/pricing.py` to fix the order of operations. The diff should touch at
most 2 files: the test file and the source file.
