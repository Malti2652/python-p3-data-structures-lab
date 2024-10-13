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
    pass
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    pass
    max_heat = max(spicy_foods, key=lambda food: food["heat_level"])[
        "heat_level"]
    return [food for food in spicy_foods if food["heat_level"] == max_heat]

def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    pass
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level = "🌶" * food["heat_level"]
            print(
                f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_average_heat_level(spicy_foods):
    pass
    if not spicy_foods:
        return 0  # Return 0 if the list is empty to avoid division by zero
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat_level / len(spicy_foods)
    return average


def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods