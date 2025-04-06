def detect_suit_combo(log_entries: list) -> list:
    """
    Detects possible suit combos from a list of decoded log entries.
    Only matches jacket and pants with same base product ID.
    Returns matched combo pairs.
    """
    pants = [e for e in log_entries if e['category'] == 'pants']
    jackets = [e for e in log_entries if e['category'] == 'jacket']

    combos = []

    for pant in pants:
        for jacket in jackets:
            if pant['base_product_id'] == jacket['base_product_id'] and pant['location'] == jacket['location']:
                combos.append({
                    "combo_id": f"{jacket['product_id']}-{pant['product_id']}",
                    "jacket": jacket,
                    "pants": pant,
                    "location": pant['location'],
                    "timestamp": pant['timestamp']
                })
                jackets.remove(jacket)
                break

    return combos
