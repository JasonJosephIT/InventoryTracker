import pytest
from src.logic.validation_rules import validate_combo_flag, validate_required_fields

def test_valid_combo_flag():
    item = {"category": "pants", "combo": True}
    assert validate_combo_flag(item) is True

def test_invalid_combo_flag():
    item = {"category": "shirt", "combo": True}
    with pytest.raises(ValueError):
        validate_combo_flag(item)

def test_missing_required_fields():
    incomplete = {
        "product_id": "P2154",
        "category": "pants"
    }
    with pytest.raises(ValueError):
        validate_required_fields(incomplete)

def test_all_required_fields_present():
    item = {
        "product_id": "P2154",
        "base_product_id": "54",
        "category": "pants",
        "change": -1,
        "location": "store-1",
        "timestamp": "2025-04-03T16:00:00Z",
        "source": "POS",
        "combo": True
    }
    assert validate_required_fields(item) is True
