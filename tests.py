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
