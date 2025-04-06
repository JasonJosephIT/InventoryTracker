from .constants import PANTS_FIT_MAP, JACKET_FIT_MAP, SHIRT_SIZE_MAP, TIE_SIZE_MAP

def decode_product_id(product_id: str) -> dict:
    if len(product_id) == 5:
        category_code = product_id[0]
        size_code = int(product_id[1])
        fit_code = int(product_id[2])
        base_product_id = product_id[3:]

        if category_code == "P":
            category = "pants"
            length = 24 + (2 * size_code)
            fit = PANTS_FIT_MAP.get(fit_code)
        elif category_code == "J":
            category = "jacket"
            length = 34 + (2 * size_code)
            fit = JACKET_FIT_MAP.get(fit_code)
        else:
            raise ValueError("Invalid 5-digit product prefix")

        return {
            "product_id": product_id,
            "base_product_id": base_product_id,
            "category": category,
            "length": length,
            "fit": fit
        }

    elif len(product_id) == 4:
        category_code = product_id[0]
        size_code = int(product_id[1])
        base_product_id = product_id[2:]

        if category_code == "S":
            category = "shirt"
            size = SHIRT_SIZE_MAP.get(size_code, "unknown")
        elif category_code == "T":
            category = "tie"
            size = TIE_SIZE_MAP.get(size_code, "unknown")
        else:
            raise ValueError("Invalid 4-digit product prefix")

        return {
            "product_id": product_id,
            "base_product_id": base_product_id,
            "category": category,
            "size": size
        }

    else:
        raise ValueError("Invalid product_id length")
