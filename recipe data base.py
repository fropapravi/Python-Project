# Auto updating program to store recipe data and user interaction to get recipe information 


def create_recipe():
    name = input("Enter the recipe name: ")
    ingredients = []
    instructions = []

    print("Enter ingredients (type 'done' when finished):")
    while True:
        ingredient = input("- ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

    print("Enter instructions (type 'done' when finished):")
    while True:
        instruction = input("- ")
        if instruction.lower() == 'done':
            break
        instructions.append(instruction)

    return {
        'name': name,
        'ingredients': ingredients,
        'instructions': instructions
    }

def add_recipe(collection, recipe):
    collection.append(recipe)

def find_recipe_by_name(collection, name):
    for recipe in collection:
        if recipe['name'].lower() == name.lower():
            return recipe
    return None

def display_recipe(recipe):
    if recipe:
        print("\nRecipe Name: ", recipe['name'])
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(" -", ingredient)
        print("Instructions:")
        for instruction in recipe['instructions']:
            print(" -", instruction)
    else:
        print("Recipe not found.")

def main():
    recipe_collection = []
    while True:
        print("\nRecipe Database")
        print("1. Add a new recipe")
        print("2. Find a recipe by name")
        print("3. Exit")

        choice = input("Choose an option (1, 2, 3): ")

        if choice == '1':
            recipe = create_recipe()
            add_recipe(recipe_collection, recipe)
            print("Recipe added successfully!")
        elif choice == '2':
            name = input("Enter the recipe name to search: ")
            recipe = find_recipe_by_name(recipe_collection, name)
            display_recipe(recipe)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
