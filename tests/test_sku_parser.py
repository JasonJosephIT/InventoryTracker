import pytest
from src.logic.sku_parser import decode_product_id

def test_decode_pants():
    result = decode_product_id("P2154")
    assert result["category"] == "pants"
    assert result["length"] == 26
    assert result["fit"] == "modern"
    assert result["base_product_id"] == "54"

def test_decode_jacket():
    result = decode_product_id("J2345")
    assert result["category"] == "jacket"
    assert result["length"] == 38
    assert result["fit"] == "normal"
    assert result["base_product_id"] == "45"

def test_decode_shirt():
    result = decode_product_id("S201")
    assert result["category"] == "shirt"
    assert result["size"] == "L"
    assert result["base_product_id"] == "01"

def test_decode_tie():
    result = decode_product_id("T102")
    assert result["category"] == "tie"
    assert result["size"] == "modern"
    assert result["base_product_id"] == "02"

def test_invalid_prefix():
    with pytest.raises(ValueError):
        decode_product_id("X102")

def test_invalid_length():
    with pytest.raises(ValueError):
        decode_product_id("T10")
