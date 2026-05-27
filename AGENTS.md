# AGENTS.md

## Project shape
Pricing utilities for an e-commerce platform. Python 3.12.

## Build and test
pytest tests/ -x --tb=short

## Task workflow
1. Write a failing test that encodes the exact behavior rule from the task spec.
2. Run it. Confirm it fails for the right reason before touching production code.
3. Make the smallest change that passes the test.
4. Run the full suite.

## Done definition
All tests pass. Diff touches ≤ 2 files.
