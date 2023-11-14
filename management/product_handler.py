from menu import products


def get_product_by_id(id: int):
    for product in products:
        if (product["_id"] == id):
            return product
    return {}


def get_products_by_type(type: str):
    products_list = []
    for product in products:
        if (product["type"] == type):
            products_list.append(product)
    return products_list


def add_product(list, **kwards):
    current_id = 0
    for item in list:
        if (item["_id"] > current_id):
            current_id = item["_id"]
    new_Product = {"_id": current_id+1, **kwards}
    list.append(new_Product)
    return new_Product
