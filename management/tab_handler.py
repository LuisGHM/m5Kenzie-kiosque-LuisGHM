from .product_handler import get_product_by_id


def calculate_tab(*args):
    price_products = []
    for arg_list in args:
        for arg in arg_list:
            product = get_product_by_id(arg["_id"])
            price_products.append(product["price"] * arg["amount"])

    result = sum(price_products)
    return round(result, 2)
