# Demo Prompt

Paste this into Claude Code to run the demo:

```
The calculate_price function applies tax and discount in the wrong order.
Fix it using TDD — write the failing test first, then fix the code.
```

## What to watch for

The AGENTS.md task workflow enforces a strict red-green cycle:
1. Write a failing test that encodes the exact rule
2. Run it — confirm it fails for the right reason
3. Make the smallest change that makes it pass
4. Run the full suite

The bug: `src/pricing.py` applies tax first, then discount. The correct order is
discount first, then tax. This matters: on a $100 item with 10% discount and 8% tax,
the wrong order gives $97.20 and the right order gives $97.20... wait, actually:
- Wrong: `(100 * 1.08) * 0.90 = $97.20`
- Right: `(100 * 0.90) * 1.08 = $97.20`

These are mathematically equal for simple cases, but the spec is explicit: discount
applies to the base price, tax applies to the discounted price. The test should
encode this as a rule, not just check the number.

This demo shows TDD as a forcing function: writing the test first makes you define
the correct behavior before you touch any production code.
