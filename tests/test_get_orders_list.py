from api.order_api import OrderApi
import allure


class TestGetOrdersList:
    @allure.title("Получение списка заказов проходит успешно")
    @allure.description("Проверяем успешное получение списка всех заказов.")
    def test_get_orders_list_success(self):
        response = OrderApi.get_orders_list()
        assert response.status_code == 200, f"Ожидался статус код 200, а вернулся {response.status_code}"
        assert "orders" in response.json(), f"В ответе отсутствует поле 'orders': {response.json()}"
        assert isinstance(response.json()["orders"], list), f"Ожидался тип 'orders' как list, а вернулся {type(response.json()['orders'])}"