def is_combo_allowed(category: str) -> bool:
    return category in {"pants", "jacket"}

def validate_combo_flag(item: dict) -> bool:
    if item.get("combo", False) and not is_combo_allowed(item["category"]):
        raise ValueError(f"Combo not allowed for category: {item['category']}")
    return True

def validate_required_fields(item: dict) -> bool:
    required_fields = ["product_id", "base_product_id", "category", "change", "location", "timestamp", "source", "combo"]
    missing = [field for field in required_fields if field not in item]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    return True
