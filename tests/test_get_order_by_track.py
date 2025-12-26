from api.order_api import OrderApi
from data import GetOrderByTrackData
import allure


class TestGetOrderByTrack:
    @allure.title("Получение заказа по треку проходит успешно")
    @allure.description("Проверяем, что можно получить заказ по треку и данные заказа корректны.")
    def test_get_order_by_track_success(self, create_order, finish_order_by_track):
        track = create_order["track"]
        response = OrderApi.get_order_by_track(track)
        finish_order_by_track.append(track)
        assert response.status_code == 200, f"Ожидался статус код 200, а вернулся {response.status_code}"
        assert "order" in response.json(), f"В ответе отсутствует поле 'order': {response.json()}"
        assert response.json()["order"]["track"] == track, f"Ожидался трек {track}, а вернулся {response.json()['order']['track']}"

    @allure.title("Получение заказа по треку без трека возвращает ошибку 400")
    @allure.description("Проверяем, что при отсутствии трека в запросе возвращается корректная ошибка.")
    def test_get_order_by_track_without_track_returns_error(self):
        response = OrderApi.get_order_by_track("")
        assert response.status_code == 400, f"Ожидался статус код 400, а вернулся {response.status_code}"
        assert response.json() == GetOrderByTrackData.GET_ORDER_BY_TRACK_NOT_ENOUGH_DATA_RESPONSE, f"Ожидался ответ {GetOrderByTrackData.GET_ORDER_BY_TRACK_NOT_ENOUGH_DATA_RESPONSE}, а вернулся {response.json()}"

    @allure.title("Получение заказа по несуществующему треку возвращает ошибку 404")
    @allure.description("Проверяем, что при запросе с несуществующим треком возвращается корректная ошибка.")
    def test_get_order_by_track_with_non_existent_track_returns_error(self):
        non_existent_track = 999999
        response = OrderApi.get_order_by_track(non_existent_track)
        assert response.status_code == 404, f"Ожидался статус код 404, а вернулся {response.status_code}"
        assert response.json() == GetOrderByTrackData.GET_ORDER_BY_TRACK_NON_EXISTENT_TRACK_RESPONSE, f"Ожидался ответ {GetOrderByTrackData.GET_ORDER_BY_TRACK_NON_EXISTENT_TRACK_RESPONSE}, а вернулся {response.json()}"