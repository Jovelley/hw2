class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit

class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []

    def add_ingredient(self, ingredient: Ingredient):
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Некорректный коэффициент")
        scaled_ingredients = []
        for ing in self.ingredients:
            scaled_ing = Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            scaled_ingredients.append(scaled_ing)
        return Recipe(self.title, scaled_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        ingredients_str = "\n".join(str(i) for i in self.ingredients)
        return f"{self.title}:\n{ingredients_str}"
    
