from data import CreateCourierData, LoginCourierData, CreateOrderData
from faker import Faker
from random import randint

class ChangeTestDataHelper:
    def modify_create_courier_body(key, value):
        body = CreateCourierData.CREATE_COURIER_DATA.copy()
        body[key] = value
        
        return body
    
    def delete_param_create_courier_body(key):
        body = CreateCourierData.CREATE_COURIER_DATA.copy()
        body.pop(key)
        return body
     
    def modify_login_courier_body(key, value):
        body = LoginCourierData.LOGIN_COURIER_DATA.copy()
        body[key] = value
        return body      
    
    def delete_param_login_courier_body(key):
        body = LoginCourierData.LOGIN_COURIER_DATA.copy()
        body.pop(key)
        return body
    
    def modify_create_order_body(key, value):
        body = CreateOrderData.CREATE_ORDER_DATA.copy()
        body[key] = value
        return body


class CourierFactory:
    @staticmethod
    def default_body_with_random_parameters():
        faker = Faker()


        return {
        "login": faker.user_name() + str(randint(1000, 9999)),
        "password": faker.password(),
        "firstName": faker.first_name() + str(randint(1000, 9999))
    }
    @staticmethod
    def login_courier_body(login, password):
        return {
            "login": login,
            "password": password
        }

class OrderFactory:
    @staticmethod
    def default_body_with_random_parameters():
        faker = Faker()
        return {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "address": faker.address(),
            "metroStation": 4,
            "phone": faker.phone_number(),
            "rentTime": randint(1,7),
            "deliveryDate": faker.date_time_this_month(after_now=True).date().isoformat()
        }