from data import LoginCourierData
from api.courier_api import CourierApi
from helper import ChangeTestDataHelper
import pytest
import allure


class TestLoginCourier:
    @allure.title("Авторизация курьера проходит успешно")
    @allure.description("Проверяем, что зарегистрированный курьер может успешно авторизоваться и получить id.")
    def test_login_courier_success(self, create_courier, cleanup_courier):
        response = CourierApi.login_courier(create_courier["body"])
        cleanup_courier.append(response.json()["id"])
        assert response.status_code == 200, f"Ожидался статус код 200, а вернулся {response.status_code}"
        assert "id" in response.json(), f"В ответе отсутствует поле 'id': {response.json()}"

    @pytest.mark.parametrize("parameter", [
        pytest.param("login"),
        pytest.param("password")
    ])
    @allure.title("Авторизация с неверным {parameter} возвращает ошибку 404")
    @allure.description("Убеждаемся, что при неверных учётных данных сервис возвращает ошибку 404 и корректное сообщение.")
    def test_login_with_wrong_credentials_returns_error(self, parameter):
        body = ChangeTestDataHelper.modify_login_courier_body(parameter, "Incorrect")
        response = CourierApi.login_courier(body)
        assert response.status_code == 404, f"Ожидался статус код 404, а вернулся {response.status_code}"
        assert response.json() == LoginCourierData.LOGIN_COURIER_WRONG_CREDENTIALS_RESPONSE, f"Ожидался ответ {LoginCourierData.LOGIN_COURIER_WRONG_CREDENTIALS_RESPONSE}, а вернулся {response.json()}"

    @pytest.mark.parametrize("parameter", [
        pytest.param("login"),
        pytest.param("password")
    ])
    @allure.title("Авторизация без обязательного поля {parameter} возвращает ошибку 400")
    @allure.description("Проверяем, что пропуск обязательного поля в запросе авторизации приводит к ошибке 400.")
    def test_login_requires_all_required_fields(self, parameter):
        body = ChangeTestDataHelper.delete_param_login_courier_body(parameter)
        response = CourierApi.login_courier(body)
        assert response.status_code == 400, f"Ожидался статус код 400, а вернулся {response.status_code}"
        assert response.json() == LoginCourierData.LOGIN_COURIER_MISSING_CREDENTIAL_RESPONSE, f"Ожидался ответ {LoginCourierData.LOGIN_COURIER_MISSING_CREDENTIAL_RESPONSE}, а вернулся {response.json()}"
