def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]


def add_or_remove_cash(total_cash, new_cash):
    total_cash["admin"]["total_cash"] += new_cash
    return total_cash["admin"]["total_cash"]


def get_pets_sold(get_pets):
    return get_pets["admin"]["pets_sold"]

def increase_pets_sold(get_pets, extra):
    get_pets["admin"]["pets_sold"] = extra
    return get_pets["admin"]["pets_sold"]


def get_stock_count(pets):
    stock_count = 0
    for pet in pets["pets"]:
        stock_count += 1
    return stock_count
