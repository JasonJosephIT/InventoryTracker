from src.logic.bundle_detection import detect_suit_combo

def test_detect_combo_pair():
    logs = [
        {"product_id": "P2154", "base_product_id": "54", "category": "pants", "location": "store-1"},
        {"product_id": "J2345", "base_product_id": "54", "category": "jacket", "location": "store-1"}
    ]
    combos = detect_suit_combo(logs)
    assert len(combos) == 1
    assert combos[0]["combo_id"] == "J2345-P2154"

def test_does_not_pair_different_locations():
    logs = [
        {"product_id": "P2154", "base_product_id": "54", "category": "pants", "location": "store-1"},
        {"product_id": "J2345", "base_product_id": "54", "category": "jacket", "location": "store-2"}
    ]
    assert detect_suit_combo(logs) == []

def test_does_not_pair_different_base_ids():
    logs = [
        {"product_id": "P2154", "base_product_id": "54", "category": "pants", "location": "store-1"},
        {"product_id": "J2345", "base_product_id": "45", "category": "jacket", "location": "store-1"}
    ]
    assert detect_suit_combo(logs) == []
