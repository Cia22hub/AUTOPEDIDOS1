from rapidfuzz import process

from utils.products import PRODUCTS


# =====================================
# BUSCAR PRODUCTO SIMILAR
# =====================================

def match_product(text):

    result = process.extractOne(
        text,
        PRODUCTS
    )

    if result:

        product = result[0]

        score = result[1]

        if score > 70:

            return product

    return None