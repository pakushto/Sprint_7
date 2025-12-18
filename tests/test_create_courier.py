from api.courier_api import CourierApi
from helper import ChangeTestDataHelper
from data import CreateCourierData
import pytest
import allure

class TestCreateCourier:
    @allure.title("Создание курьера проходит успешно")
    @allure.description("Проверяем успешное создание нового курьера и возможность авторизации с его учетными данными.")
    def test_create_courier_success(self, courier_body, cleanup_courier):
        create_courier_response = CourierApi.create_courier(courier_body)
        login_courier_response = CourierApi.login_courier(courier_body)
        cleanup_courier.append(login_courier_response.json()["id"])
        assert create_courier_response.status_code == 201, f"Ожидался статус код 201, а вернулся {create_courier_response.status_code}" 
        assert create_courier_response.json() == CreateCourierData.CREATE_COURIER_SUCCESSFUL_RESPONSE, f"Ожидался ответ {CreateCourierData.CREATE_COURIER_SUCCESSFUL_RESPONSE}, а вернулся {create_courier_response.json()}"
        assert login_courier_response.status_code == 200, f"Ожидался статус код 200, а вернулся {login_courier_response.status_code}"

    @allure.title("Нельзя создать курьера с существующим логином")
    @allure.description("Убеждаемся, что при повторной попытке создать курьера с тем же логином возвращается ошибка 409.")
    def test_cannot_create_duplicate_courier(self, courier_body):
        CourierApi.create_courier(courier_body)
        create_courier_response = CourierApi.create_courier(courier_body)
        assert create_courier_response.status_code == 409, f"Ожидался статус код 409, а вернулся {create_courier_response.status_code}"
        assert create_courier_response.json() == CreateCourierData.CREATE_COURIER_DUPLICATE_ERROR_RESPONSE, f"Ожидался ответ {CreateCourierData.CREATE_COURIER_DUPLICATE_ERROR_RESPONSE}, а вернулся {create_courier_response.json()}"
    
    @pytest.mark.parametrize("parameter", [
        pytest.param("login"),
        pytest.param("password"),
        pytest.param("firstName")
    ])
    @allure.title("Создание курьера без обязательного параметра {parameter} возвращает ошибку 400")
    @allure.description("Проверяем, что пропуск обязательного поля приводит к ответу 400 и корректному сообщению об ошибке.")
    def test_courier_creation_requires_all_required_fields(self, parameter):
        create_courier_body = ChangeTestDataHelper.delete_param_create_courier_body(parameter)
        create_courier_response = CourierApi.create_courier(create_courier_body)
        assert create_courier_response.status_code == 400, f"Ожидался статус код 400, а вернулся {create_courier_response.status_code}"
        assert create_courier_response.json() == CreateCourierData.CREATE_COURIER_MISSING_PARAMETERS_RESPONSE, f"Ожидался ответ {CreateCourierData.CREATE_COURIER_MISSING_PARAMETERS_RESPONSE}, а вернулся {create_courier_response.json()}"


