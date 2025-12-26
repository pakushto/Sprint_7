# Sprint_7 — автотесты API “Scooter”

Набор API‑тестов на `pytest` для сервиса “Scooter” (Praktikum). Тесты покрывают основные сценарии по курьерам и заказам: создание/логин/удаление курьера, создание заказа, получение заказа по треку, список заказов, принятие и завершение заказа.

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
- `conftest.py` — фикстуры:
  - `create_courier`, `login_courier` — возвращают callables, чтобы вызывать API с переданным body;
  - `create_and_login_courier` — создаёт курьера, логинится и отдаёт `id` + тела ответов;
  - `cleanup_courier` — собирает id курьеров для удаления после теста;
  - `create_order`, `get_order_by_track`, `finish_order`, `finish_order_by_track` — вспомогательные фикстуры для работы с заказами.
- `data.py` — ожидаемые ответы/тестовые константы
- `helper.py` — генераторы/хелперы данных (`CourierFactory`, `OrderFactory`, `ChangeTestDataHelper`) с использованием `faker` для случайных значений
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
