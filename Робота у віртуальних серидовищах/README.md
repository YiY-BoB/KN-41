# Звіт до роботи

## Тема: _Робота у віртуальних середовищах (Python Virtual Environments)_

### Мета роботи: _Навчитись створювати та використовувати віртуальні середовища у Python-проєктах з використанням pip, venv, poetry або pipenv; встановлювати залежності, керувати пакетами та організовувати середовище для розробки._

---

### Виконання роботи

1. **Розробили ізольоване середовище Python за допомогою `venv`**:
    - Виконано команду:
      ```bash
      python -m venv venv
      ```
    - Активовано середовище:
      ```bash
      source venv/bin/activate  # Linux/macOS
      venv\Scripts\activate    # Windows
      ```
    - Встановлено пакет `requests`:
      ```bash
      pip install requests
      ```
    - Створено файл `requirements.txt`:
      ```bash
      pip freeze > requirements.txt
      ```

2. **Використання `pipenv`**:
    - Ініціалізація середовища:
      ```bash
      pipenv --python 3.12
      pipenv install requests
      pipenv shell
      ```
    - Сформовано файл `Pipfile` та `Pipfile.lock` автоматично.

3. **Ініціалізація середовища з `poetry`**:
    - Команди виконання:
      ```bash
      poetry init
      poetry add requests
      poetry install
      poetry shell
      ```
    - Одержано файл `pyproject.toml` та контроль версій залежностей.

4. **Перевірено роботу встановлених бібліотек** через тестовий код:
    ```python
    import requests
    response = requests.get("https://httpbin.org/get")
    print(response.json())
    ```
    - Програма вивела валідну відповідь у форматі JSON.

5. **Організовано структуру проєкту**:
    - Додано папки: `src`, `tests`, `venv` (ігноровано через `.gitignore`).
    - Створено `README.md` та проєктні файли у репозиторії GitHub.

6. **Вставлені скріншоти у папку `pictures/`**:
    ![venv активація](./pictures/venv_activate.png)
    ![pipenv shell](./pictures/pipenv_shell.png)
    ![poetry init](./pictures/poetry_init.png)
    ![виконання тесту](./pictures/test_output.png)

7. **Тестовий код**:
    ```python
    import requests

    def fetch_data():
        response = requests.get("https://api.github.com")
        return response.status_code

    print(fetch_data())
    ```

---

### Висновок:
> у висновку потрібно відповісти на запитання:

- **Що зроблено в роботі:** Ознайомлено з трьома способами створення віртуальних середовищ у Python.
- **Чи досягнуто мети роботи:** Так, навченося використовувати `venv`, `pipenv`, `poetry`, а також керувати залежностями.
- **Які нові знання отримано:** Структура середовищ, типові команди, файл `pyproject.toml`, переваги кожного інструмента.
- **Чи вдалось відповісти на всі питання:** Так, виконано інструкції з офіційного ресурсу.
- **Чи вдалося виконати всі завдання:** Так, середовище створено, бібліотеки протестовано, проект організовано.
- **Чи виникли складності:** Так, незначні при використанні `pipenv` на Windows (використано альтернативу через `poetry`).
- **Чи подобається формат:** Так, зрозуміло і зручно, з фокусом на практику.
- **Побажання:** Було б корисно додати коротке відео-демо процесу або анімації команд.

---

