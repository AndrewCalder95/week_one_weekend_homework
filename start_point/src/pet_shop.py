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

def get_pets_by_breed(pets, breed_search):
    amount_of_breed = []
    for pet in pets["pets"]:
        if pet["breed"] == breed_search:
            amount_of_breed.append(pet)
    return amount_of_breed
            
def find_pet_by_name(pets,name):
    found_pet = {"name" : "None"}
    for pet in pets["pets"]:
        if pet["name"] == name:
            found_pet["name"] = pet
            return found_pet["name"]
        