from menu import products


def get_product_by_id(id: int):
    i = 0
    for product in products:
        if (product["_id"] == id):
            return product
        i+1
    return {}


def get_products_by_type(type: str):
    i = 0
    products_list = []
    for product in products:
        if (product["type"] == type):
            products_list.append(product)
        i+1
    return products_list
