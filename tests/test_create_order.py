from data import CreateOrderData
from api.order_api import OrderApi
from helper import ChangeTestDataHelper
import pytest
import allure


class TestCreateOrder:
    @allure.title("Создание заказа проходит успешно")
    @allure.description("Проверяем базовый позитивный сценарий создания заказа и получение track.")
    def test_create_order_success(self, finish_order_by_track):
        create_order_response = OrderApi.create_order(CreateOrderData.CREATE_ORDER_DATA)
        finish_order_by_track.append(create_order_response.json()["track"])
        assert create_order_response.status_code == 201, f"Ожидался статус код 201, а вернулся {create_order_response.status_code}"
        assert "track" in create_order_response.text, f"В ответе отсутствует поле 'track': {create_order_response.text}"

    @pytest.mark.parametrize('color', [
        pytest.param(["BLACK"]),
        pytest.param(["GREY"]),
        pytest.param(["BLACK", "GREY"]),
        pytest.param([])
    ])
    @allure.title("Создание заказа с цветами {color}")
    @allure.description("Убеждаемся, что заказ можно создать с разными вариантами массива цветов.")
    def test_create_order_with_various_color_options(self, color, finish_order_by_track):
        body = ChangeTestDataHelper.modify_create_order_body("color", color)
        response = OrderApi.create_order(body)
        finish_order_by_track.append(response.json()["track"])
        assert response.status_code == 201, f"Ожидался статус код 201, а вернулся {response.status_code}"
        assert "track" in response.text, f"В ответе отсутствует поле 'track': {response.text}"
