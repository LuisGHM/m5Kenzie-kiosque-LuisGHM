from menu import products


def get_product_by_id(id: int):
    i = 0
    for product in products:
        if (product["_id"] == id):
            return product
        i+1
    return {}


def get_products_by_type(type: str):
    return products[1]["_id"]
