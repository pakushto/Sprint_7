# Sprint_7 — автотесты API “Scooter”

Набор API‑тестов на `pytest` для сервиса “Scooter” (Praktikum). Тесты проверяют основные сценарии по курьерам и заказам: создание/логин/удаление курьера, создание заказа, получение заказа по треку, список заказов, принятие заказа курьером.

Базовый URL стенда задаётся в `urls.py`.

## Стек

- Python 3
- `pytest`
- `requests`
- `allure-pytest`
- `faker`

Зависимости фиксируются в `requirements.txt`.

## Структура проекта

- `api/` — простые клиенты для ручек API (`CourierApi`, `OrderApi`)
- `tests/` — тесты
- `conftest.py` — фикстуры (создание/логин курьера, создание заказа, уборка данных)
- `data.py` — ожидаемые ответы/тестовые константы
- `helper.py` — генераторы/хелперы данных (`CourierFactory`, `OrderFactory`)
- `urls.py` — все URL-ы ручек

## Быстрый старт

1) Создать и активировать виртуальное окружение:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Установить зависимости:

```bash
pip install -r requirements.txt
```

3) Запустить тесты:

```bash
pytest -q
```

## Запуск с Allure

1) Сгенерировать результаты:

```bash
pytest --alluredir=allure_results
```

2) Открыть отчёт (нужен установленный Allure CLI):

```bash
allure serve allure_results
```

## Настройка стенда

По умолчанию используется стенд:

- `https://qa-scooter.praktikum-services.ru`

Если нужно изменить окружение — обнови `Urls.BASE_URL` в `urls.py`.
