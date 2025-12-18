import requests
from urls import Urls

class CourierApi:
    @staticmethod
    def create_courier(body):
        return requests.post(Urls.CREATE_COURIER_URL, json=body)
    
    @staticmethod
    def login_courier(body):
        return requests.post(Urls.LOGIN_COURIER_URL, json=body)
    
    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(Urls.DELETE_COURIER_URL.format(courier_id=courier_id))
    

