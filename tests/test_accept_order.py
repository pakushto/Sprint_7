import allure
from api.order_api import OrderApi
from data import AcceptOrderData


class TestAcceptOrder:
    @allure.title("Успешное принятие заказа курьером")
    @allure.description("Проверяем, что курьер может успешно принять заказ и получить корректный ответ.")
    def test_accept_order_success(self, create_and_login_courier, get_order_by_track, cleanup_courier, finish_order):
        courier_id = create_and_login_courier["id"]
        order_id = get_order_by_track["order_id"]
        response = OrderApi.accept_order(order_id, courier_id)
        cleanup_courier.append(courier_id)
        finish_order.append(order_id)
        assert response.status_code == 200, f"Ожидался статус код 200, а вернулся {response.status_code}"
        assert response.json() == AcceptOrderData.ACCEPT_ORDER_RESPONSE, f"Ожидался ответ {AcceptOrderData.ACCEPT_ORDER_RESPONSE}, а вернулся {response.json()}"

    @allure.title("Нельзя принять заказ без указания ID курьера")
    @allure.description("Проверяем, что попытка принять заказ без указания ID курьера возвращает ошибку 400.")
    def test_accept_order_without_courier_id_returns_error(self, get_order_by_track, finish_order):
        order_id = get_order_by_track["order_id"]
        response = OrderApi.accept_order(order_id, "")
        finish_order.append(order_id)
        assert response.status_code == 400, f"Ожидался статус код 400, а вернулся {response.status_code}"
        assert response.json() == AcceptOrderData.ACCEPT_ORDER_NOT_ENOUGH_DATA_RESPONSE, f"Ожидался ответ {AcceptOrderData.ACCEPT_ORDER_NOT_ENOUGH_DATA_RESPONSE}, а вернулся {response.json()}"

    @allure.title("Нельзя принять заказ без указания ID заказа")
    @allure.description("Проверяем, что попытка принять заказ без указания ID заказа возвращает ошибку 400.")
    def test_accept_order_without_order_id_returns_error(self, create_and_login_courier, cleanup_courier):
        courier_id = create_and_login_courier["id"]
        response = OrderApi.accept_order("", courier_id)
        cleanup_courier.append(courier_id)
        assert response.status_code == 400, f"Ожидался статус код 400, а вернулся {response.status_code}"
        assert response.json() == AcceptOrderData.ACCEPT_ORDER_NOT_ENOUGH_DATA_RESPONSE, f"Ожидался ответ {AcceptOrderData.ACCEPT_ORDER_NOT_ENOUGH_DATA_RESPONSE}, а вернулся {response.json()}"

    @allure.title("Нельзя принять несуществующий заказ")
    @allure.description("Проверяем, что попытка принять несуществующий заказ возвращает ошибку 404.")
    def test_accept_order_with_non_existent_order_id_returns_error(self, create_and_login_courier, cleanup_courier):
        courier_id = create_and_login_courier["id"]
        non_existent_order_id = 999999
        response = OrderApi.accept_order(non_existent_order_id, courier_id)
        cleanup_courier.append(courier_id)
        assert response.status_code == 404, f"Ожидался статус код 404, а вернулся {response.status_code}"
        assert response.json() == AcceptOrderData.ACCEPT_ORDER_NON_EXISTENT_ORDER_ID_RESPONSE, f"Ожидался ответ {AcceptOrderData.ACCEPT_ORDER_NON_EXISTENT_ORDER_ID_RESPONSE}, а вернулся {response.json()}"

    @allure.title("Нельзя принять заказ несуществующим курьером")
    @allure.description("Проверяем, что попытка принять заказ несуществующим курьером возвращает ошибку 404.")
    def test_accept_order_with_non_existent_courier_id_returns_error(self, get_order_by_track, finish_order):
        order_id = get_order_by_track["order_id"]
        non_existent_courier_id = 999999
        response = OrderApi.accept_order(order_id, non_existent_courier_id)
        finish_order.append(order_id)
        assert response.status_code == 404, f"Ожидался статус код 404, а вернулся {response.status_code}"
        assert response.json() == AcceptOrderData.ACCEPT_ORDER_NON_EXISTENT_COURIER_ID_RESPONSE, f"Ожидался ответ {AcceptOrderData.ACCEPT_ORDER_NON_EXISTENT_COURIER_ID_RESPONSE}, а вернулся {response.json()}"

