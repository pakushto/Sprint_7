import requests
import allure
from urls import Urls

class CourierApi:
    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(body):
        return requests.post(Urls.CREATE_COURIER_URL, json=body)
    
    @staticmethod
    @allure.step("Авторизация курьера")
    def login_courier(body):
        return requests.post(Urls.LOGIN_COURIER_URL, json=body)
    
    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(Urls.DELETE_COURIER_URL.format(courier_id=courier_id))
    

