def main(recipe, available_ingredients):
    max_cakes = float('inf')
    for ingredient, amount in recipe.items():
        if ingredient not in available_ingredients:
            return 0
        max_cakes = min(max_cakes, available_ingredients[ingredient] // amount)
    return max_cakes