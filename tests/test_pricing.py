import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.pricing import calculate_total, line_item_total, apply_promo


def test_line_item_total():
    assert line_item_total(3, 9.99) == 29.97

def test_apply_promo_save10():
    assert apply_promo(100.0, "SAVE10") == 90.0

def test_apply_promo_unknown_code():
    assert apply_promo(100.0, "FAKE99") == 100.0

def test_calculate_total_no_discount_no_tax():
    assert calculate_total(100.0, 0.0, 0.0) == 100.0

def test_calculate_total_tax_only():
    assert calculate_total(100.0, 0.0, 0.20) == 120.0
