import allure
from api.courier_api import CourierApi
from data import DeleteCourierData


class TestDeleteCourier:
    @allure.title("Удаление курьера проходит успешно")
    @allure.description("Проверяем успешное удаление созданного курьера и невозможность авторизации с его учетными данными.")
    def test_delete_courier_success(self, create_and_login_courier):
        delete_courier_response = CourierApi.delete_courier(create_and_login_courier["id"])
        login_courier_response = CourierApi.login_courier(create_and_login_courier["body"])
        assert delete_courier_response.status_code == 200, f"Ожидался статус код 200, а вернулся {delete_courier_response.status_code}"
        assert delete_courier_response.json() == DeleteCourierData.DELETE_COURIER_RESPONSE, f"Ожидался ответ {DeleteCourierData.DELETE_COURIER_RESPONSE}, а вернулся {delete_courier_response.json()}"
        assert login_courier_response.status_code == 404, f"Ожидался статус код 404, а вернулся {login_courier_response.status_code}"

    @allure.title("Удаление курьера без id возвращает ошибку 400")
    @allure.description("Отправляем DELETE без подстановки id в URL и ожидаем 404 с сообщением Недостаточно данных для удаления курьера.")
    def test_delete_courier_without_id_returns_error(self):
        delete_courier_response = CourierApi.delete_courier(courier_id="")
        assert delete_courier_response.status_code == 400, f"Ожидался статус код 400, а вернулся {delete_courier_response.status_code}"
        assert delete_courier_response.json() == DeleteCourierData.DELETE_COURIER_WITHOUT_ID_RESPONSE, f"Ожидался ответ {DeleteCourierData.DELETE_COURIER_WITHOUT_ID_RESPONSE}, а вернулся {delete_courier_response.json()}"
    
    @allure.title("Удаление с несуществующим id возвращает ошибку 404")
    @allure.description("Удаляем курьера, затем повторяем удаление по тому же id и получаем корректную ошибку 404.")
    def test_delete_courier_with_non_existent_id_returns_error(self, create_and_login_courier):
        CourierApi.delete_courier(create_and_login_courier["id"])
        delete_courier_response = CourierApi.delete_courier(create_and_login_courier["id"])
        assert delete_courier_response.status_code == 404, f"Ожидался статус код 404, а вернулся {delete_courier_response.status_code}"
        assert delete_courier_response.json() == DeleteCourierData.DELETE_COURIER_NON_EXISTENT_ID_RESPONSE, f"Ожидался ответ {DeleteCourierData.DELETE_COURIER_NON_EXISTENT_ID_RESPONSE}, а вернулся {delete_courier_response.json()}"