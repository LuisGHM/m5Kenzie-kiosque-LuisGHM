from menu import products


def verify_type_str(variable):
    if not isinstance(variable, str):
        raise TypeError("Type must be a str.")
    return variable


def verify_type_int(variable):
    if not isinstance(variable, int):
        raise TypeError("product id must be an int.")
    return variable


def get_product_by_id(id):
    try:
        id = verify_type_int(id)
        for product in products:
            if product["_id"] == id:
                return product
        return {}
    except TypeError:
        raise TypeError("product id must be an int")

def get_products_by_type(type_str):
    try:
        verify_type_str(type_str)
        products_list = []
        for product in products:
            if product["type"] == type_str:
                products_list.append(product)
        return products_list
    except TypeError:
        raise TypeError("product type must be a str")


def add_product(list, **kwards):
    current_id = 0
    for item in list:
        if (item["_id"] > current_id):
            current_id = item["_id"]
    new_Product = {"_id": current_id+1, **kwards}
    list.append(new_Product)
    return new_Product


def menu_report():
    product_count = len(products)

    values = [n["price"] for n in products]
    average = sum(values) / len(values)

    type_count = {}
    for product in products:
        product_type = product["type"]
        type_count[product_type] = type_count.get(product_type, 0) + 1
    most_common_type = max(type_count, key=type_count.get)

    return f"Products Count: {product_count} - Average Price: ${round(average, 2)} - Most Common Type: {most_common_type}"
