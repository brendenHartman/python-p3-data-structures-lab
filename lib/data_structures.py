spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [name["name"] for name in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        name = item["name"]
        cuisine = item["cuisine"]
        heat = item["heat_level"]
        peps = "🌶" * heat
        print(f"{name} ({cuisine}) | Heat Level: {peps}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    found = [item for item in spicy_foods if cuisine == item["cuisine"]]
    return found[0]

def print_spiciest_foods(spicy_foods):
    food_printed = [food for food in spicy_foods if food["heat_level"] > 5]
    print_spicy_foods(food_printed)

def get_average_heat_level(spicy_foods):
    avg = 0
    count = 0
    for food in spicy_foods:
        avg += food["heat_level"]
        count += 1
    avg = avg / count
    return avg
            

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
