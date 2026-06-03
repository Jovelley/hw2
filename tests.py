import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

class TestIngredient:

    def test_creation():
        ingredient = Ingredient("Мука", 500, "г")
        assert ingredient.name == "Мука"
        assert ingredient.quantity == 500.0
        assert ingredient.unit == "г"

    def test_negative_quantity(self):
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            Ingredient("Мука", -100, "г")

    def test_str():
        ingredient = Ingredient("Мука", 500, "г")
        assert str(ingredient) == "Мука: 500.0 г"

    def test_equal_same_name_and_unit():
        i1 = Ingredient("Мука", 500, "г")
        i2 = Ingredient("Мука", 300, "г")
        assert i1 == i2

    def test_not_equal_different_name():
        i1 = Ingredient("Мука", 500, "г")
        i2 = Ingredient("Сахар", 500, "г")
        assert i1 != i2

    def test_not_equal_different_unit():
        i1 = Ingredient("Мука", 500, "г")
        i2 = Ingredient("Мука", 500, "кг")
        assert i1 != i2


class TestRecipe:
    def test_creation(self):
        ing = Ingredient("Мука", 500, "г")
        recipe = Recipe("Пицца", [ing])
        assert recipe.title == "Пицца"
        assert len(recipe.ingredients) == 1

    def test_recipe_creation():
        recipe = Recipe("Пицца")
        assert recipe.title == "Пицца"
        assert recipe.ingredients == []

    def test_add_new_ingredient():
        recipe = Recipe("Пицца")
        ingredient = Ingredient("Сыр", 100, "г")
        recipe.add_ingredient(ingredient)
        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0] == ingredient
        assert recipe.ingredients[0].quantity == 100

    def test_is_valid_ratio(self):
        assert Recipe.is_valid_ratio(2.5) == True
        assert Recipe.is_valid_ratio(-1) == False
        assert Recipe.is_valid_ratio(0) == False
        assert Recipe.is_valid_ratio("не число") == False

    def test_add_existing_ingredient():
        recipe = Recipe("Пицца")
        recipe.add_ingredient(Ingredient("Сыр", 100, "г"))
        recipe.add_ingredient(Ingredient("Сыр", 50, "г"))
        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0].quantity == 150

    def test_scale_returns_new_recipe():
        recipe = Recipe("Тесто", [Ingredient("Мука", 100, "г")])
        scaled = recipe.scale(2)
        assert scaled is not recipe
        assert scaled.ingredients[0].quantity == 200
        assert recipe.ingredients[0].quantity == 100

    def test_scale_invalid_ratio():
        recipe = Recipe("Тесто",[Ingredient("Мука", 100, "г")])
        with pytest.raises(ValueError):
            recipe.scale(0)

    def test_recipe_len():
        recipe = Recipe("Салат")
        recipe.add_ingredient(Ingredient("Помидор", 2, "шт"))
        recipe.add_ingredient(Ingredient("Огурец", 1, "шт"))
        assert len(recipe) == 2
