# Система управления рецептами
 
# Описание
Учебный проект по ООП и тестированию.  
Реализация классов для работы с рецептами, ингредиентами и списками покупок,. Тестирование созданных классов
Проект представляет собой простую систему управления рецептами и списками покупок.  
Он позволяет добавлять ингредиенты, масштабировать рецепты, объединять их в список покупок и анализировать количество необходимых продуктов.

# Использование
Структура проекта
project
├── recipes.py             # Основные классы
├── test_recipes.py        # Тесты
├── requirements.txt       # Зависимости
├── .gitignore             # Игнорируемые файлы
└── README.md              # Документация

## Использование
Пример использования программы (recipes.py)
```python
from recipes import Ingredient, Recipe, ShoppingList

if __name__ == "__main__":
    recipe = Recipe("Пицца", [Ingredient("Сыр", 100, "г"),Ingredient("Тесто", 200, "г")])
    shopping = ShoppingList()
    shopping.add_recipe(recipe, 2)
    print(shopping.get_list())
```
### Установка 
py -m pip install -r requirements.txt
## Запуск тестов
py -m pytest -v
```bash
git clone hw2
cd project
pip install -r requirements.txt
pytest
```
## Автор 
Кутаева Варвара Сергеевна ТАДБ252
