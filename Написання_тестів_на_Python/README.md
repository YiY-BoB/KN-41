# Звіт до роботи

## Тема: _Тестування в Python: assert, unittest, pytest, coverage_

### Мета роботи: _Ознайомитися з методами тестування в Python, навчитися використовувати інструменти перевірки коду, створювати unit-тести, працювати з бібліотеками `unittest`, `pytest`, `coverage`, а також формувати звітність._

---

### Виконання роботи

1. **Виконано перевірку даних за допомогою `assert`**:
    - Створено прості приклади з `input()` та з об'єктами класів.
    - Перевірено умови, в яких відбувається виклик помилок при некоректних значеннях.

2. **Створено класи з валідацією аргументів**:
    - Виконано валідацію у класі `Figure` з допустимими типами фігур та довжиною.
    - У класі `Name` реалізовано перевірку імені та обов’язковість хобі.

3. **Виконано юніт-тестування з бібліотекою `unittest`**:
    - Створено модуль `test.py`.
    - Написано кілька тестів: на тип фігури, довжину, обробку помилок.
    - Виявлено помилку у методі `get_figure_length` (повертав `type` замість `length`).

4. **Написано додаткову функціональність (наприклад, властивість `get_angles`) та протестовано її.**

5. **Інстальовано та використано бібліотеку `pytest`**:
    - Написано тест-функцію `test_app_triangle`.
    - Виконано запуск `pytest` через `poetry`.

6. **Проведено аналіз покриття коду з `coverage` та `pytest-cov`**:
    - Визначено рівень покриття функцій і проперті.
    - Згенеровано html-звіт для візуалізації результатів.

---

## 1. Перевірка assert при вводі з клавіатури
```python
a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"введене число: {a}")
```

## 2. Валідація у класі + assert/raise
```python
class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Богдан", "Анонім", "Євген"]:
            raise ValueError("Дозволені імена: Богдан, Анонім, Євген")
        assert hobby.strip() != "", "Хоббі не може бути пустим!"
        self.name = name
        self.hobby = hobby
```

## 3. Юніт-тести з unittest
**Файл: `app.py`**
```python
class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    def __init__(self, type, length) -> None:
        assert length > 0
        assert type in self.FIGURES
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length

    @property
    def get_angles(self):
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        if self.type == "трикутник":
            return 3
```

**Файл: `test.py`**
```python
import unittest
from random import choice, randint
from app import Figure

class TestFigure(unittest.TestCase):
    def setUp(self):
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)

    def test_figure_type(self):
        self.assertEqual(self.figure, self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(self.length, self.obj.get_figure_length)

    def test_invalid_type(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_get_angles(self):
        fig = Figure("трикутник", 1)
        self.assertEqual(fig.get_angles, 3)

if __name__ == '__main__':
    unittest.main()
```

## 4. PyTest
```bash
poetry run pytest app.py
```
**Тест-функцiя:**
```python
def test_app_triangle():
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig
```

## 5. Coverage
```bash
poetry run coverage run -m pytest test.py
poetry run coverage report
poetry run coverage html  # Відкриваємо index.html
```

## 6. Git
```bash
echo __pycache__/ >> .gitignore
echo htmlcov/ >> .gitignore
```

---


### Висновок

- **Що зроблено в роботі**: Реалізовано повний цикл тестування Python-коду, включно з ручними перевірками (`assert`), юніт-тестами (`unittest`, `pytest`) і оцінкою покриття (`coverage`).
- **Чи досягнуто мети роботи**: Так, було опановано основи тестування в Python.
- **Які нові знання отримано**: Робота з `unittest`, побудова тестів, організація структури проєкту, запуск тестів із середовища розробки та терміналу.
- **Чи вдалося відповісти на всі питання задані в ході роботи**: Так.
- **Чи вдалося виконати всі завдання**: Так, виконано всі завдання, включно з додатковими перевірками та розширенням функціоналу.
- **Чи виникли складності у виконанні завдання**: Складності виникали лише при інтеграції `pytest-cov`, але були успішно усунуті.
- **Чи подобається такий формат здачі роботи (Feedback)**: Так, практичний підхід із гітом, README та автоматизацією дуже зручний.
- **Побажання для покращення (Suggestions)**: Було б корисно побачити приклади помилок у тестах для їх аналізу та пояснення.

