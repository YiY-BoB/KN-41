# Звіт до роботи

## Тема: _Автоматизація процесу тестування з використанням GitHub Actions_

### Мета роботи: _Ознайомитись з основами CI/CD у GitHub, навчитись створювати, змінювати та запускати Workflow у репозиторії проєкту для автоматичного виконання дій, таких як запуск Python-скриптів та юніт-тестів._

---

### Виконання роботи

**1. Створення першого Workflow**
- Ініціалізовано GitHub Actions через вкладку `Actions`.
- Обрано шаблон `Python application`, змінено ім’я Workflow.
- Збережено файл `.github/workflows/main.yml` у репозиторії.

**2. Редагування Workflow та запуск коду Python**
```yml
- name: Run Python script
  run: |
    python lab.py
```
- Записано скрипт `lab.py`, додано до репозиторію.
- Workflow виконується успішно — скрипт запускається автоматично після коміту.

**3. Запуск Workflow вручну та за розкладом**
```yml
on:
  workflow_dispatch:
  schedule:
    - cron: '30 8 * * 1'  # щопонеділка о 08:30
```
- Додано ручний тригер та плановий запуск у файлі `actions.yml`.

**4. Створення декількох Workflow та Job**
```yml
jobs:
  job1:
    name: Echo First
    steps:
      - name: First Step
        run: echo "First"
  job2:
    name: Echo Second
    steps:
      - name: Second Step
        run: echo "Second"
```
- Створено два workflow-файли: `workflow_one.yml` та `workflow_two.yml`.
- Перевірено у вкладці `Actions`, обидва Workflow з’явились та запускаються окремо.

**5. Використання умов виконання кроків**
```yml
- name: Conditional Hello
  run: echo "Hello ${{ github.event.inputs.name }}"
  if: github.event.inputs.name != 'Executer'
```
- Тест виконання умовного кроку залежно від введеного параметра.

**6. Додавання баджів (Badge)**
```markdown
[![CI Status](https://github.com/USERNAME/REPO/actions/workflows/main.yml/badge.svg)](https://github.com/USERNAME/REPO/actions/workflows/main.yml)
```
- Бадж вставлено у початок `README.md`, виводить статус виконання Workflow.

**7. Інтеграція з Coverage через Codecov**
```yml
- name: Generate Report
  run: |
    coverage run -m unittest
    coverage xml

- name: Upload Coverage to Codecov
  uses: codecov/codecov-action@v3
```
- Проведено зв’язок з Codecov.
- Звіт про покриття автоматично надсилається та виводиться баджем у README.

---

### Висновок:

- **Що зроблено в роботі:** Створено, налаштовано та протестовано декілька GitHub Workflow для автоматизації запуску скриптів, юніт-тестів та перевірки покриття.
- **Чи досягнуто мети роботи:** Так, виконано повний цикл налаштування CI на GitHub.
- **Які нові знання отримано:** Поняття Job, Steps, Cron, Badge, Coverage, Workflow, Codecov; використання YAML.
- **Чи вдалось відповісти на всі питання:** Так, інструкції реалізовано згідно методички.
- **Чи вдалося виконати всі завдання:** Так, перевірено усі функціональні можливості GitHub Actions.
- **Чи виникли складності:** Невеликі затримки через синхронізацію Codecov, які були вирішені.
- **Чи подобається формат:** Так, зручний формат автоматизації, мінімум ручних дій.
- **Побажання:** Додати приклади з Docker або інтеграцією в реальні проєкти.

---

