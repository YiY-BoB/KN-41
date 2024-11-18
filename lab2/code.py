# Просте присвоєння змінних різних типів даних
a = "змінна з текстом"  # рядок (str)
b = 1  # ціле число (int)
b1 = 1.1  # число з плаваючою крапкою (float)
c = ["a", 1, 1.25, "Слово", a]  # список (list)
d = {"a": "Слово", "b": 1, a: b}  # словник (dict)
e = ("a", a)  # кортеж (tuple)
f = {"ss", a + str(b)}  # множина (set)

print(a, b, b1, c, d, e, f)

print("Перша константа: ", True)
print("Друга константа: ", None)
print(f"Константа зі змінною {False}")

print("Модуль числа -12.5:", abs(-12.5))
print("Максимальне значення серед чисел 5, 10 і -3:", max(5, 10, -3))
print("Сума чисел 1, 2 і 3:", sum([1, 2, 3]))

# Приклад з циклом for
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")

# Приклад з циклом while
count = 0
while count < 3:
    print(f"Поточне значення лічильника: {count}")
    count += 1

A = True
print("Значить A=True" if A else "Значить A=False")

number = 5
if number > 0:
    print("Число додатнє")
elif number < 0:
    print("Число від’ємне")
else:
    print("Число дорівнює нулю")

A = 0
try:
    print("Що буде якщо", 10 / A, "?")
except ZeroDivisionError as e:
    print("Помилка ділення на нуль:", e)
finally:
    print("Цей блок виконується завжди!")

try:
    with open("README.md", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Файл не знайдено!")

# Приклад використання лямбда-функції
this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Євген', 'Бувшик'))

# Інший приклад лямбда-функції для додавання двох чисел
add = lambda x, y: x + y
print("Сума 5 і 3 за допомогою лямбда-функції:", add(5, 3))