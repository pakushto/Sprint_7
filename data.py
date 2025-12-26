class CreateCourierData:
    CREATE_COURIER_DATA = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }
    CREATE_COURIER_SUCCESSFUL_RESPONSE = {
        "ok": True
    }
    
    CREATE_COURIER_DUPLICATE_ERROR_RESPONSE = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."
    }

    CREATE_COURIER_MISSING_PARAMETERS_RESPONSE = {
    "code": 400,
    "message": "Недостаточно данных для создания учетной записи"
}


class LoginCourierData:
    LOGIN_COURIER_DATA = {
        "login": "maksim_perunkov",
        "password": "Pass1515#"
    }

    LOGIN_COURIER_RESPONSE = {
        "id": 666205
    }

    LOGIN_COURIER_WRONG_CREDENTIALS_RESPONSE = {
        "code": 404,
        "message": "Учетная запись не найдена"
    }

    LOGIN_COURIER_MISSING_CREDENTIAL_RESPONSE = {
        "code": 400,
        "message": "Недостаточно данных для входа"
    }

class CreateOrderData:
    CREATE_ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"],
    }

class DeleteCourierData:
    DELETE_COURIER_RESPONSE = {
        "ok":True
    }

    DELETE_COURIER_WITHOUT_ID_RESPONSE = {
        "code": 400,
        "message": "Недостаточно данных для удаления курьера"
    }

    DELETE_COURIER_NON_EXISTENT_ID_RESPONSE = {
        "code": 404,
        "message": "Курьера с таким id нет."
    }

class AcceptOrderData:
    ACCEPT_ORDER_RESPONSE = {
        "ok":True
    }

    ACCEPT_ORDER_NOT_ENOUGH_DATA_RESPONSE = {
        "code": 400,
        "message":  "Недостаточно данных для поиска"
    }

    ACCEPT_ORDER_NON_EXISTENT_ORDER_ID_RESPONSE = {
        "code": 404,
        "message": "Заказа с таким id не существует"
    }

    ACCEPT_ORDER_NON_EXISTENT_COURIER_ID_RESPONSE = {
        "code": 404,
        "message": "Курьера с таким id не существует"
    }

class GetOrderByTrackData:
    GET_ORDER_BY_TRACK_NOT_ENOUGH_DATA_RESPONSE = {
        "code": 400,
        "message": "Недостаточно данных для поиска"
    }

    GET_ORDER_BY_TRACK_NON_EXISTENT_TRACK_RESPONSE = {
        "code": 404,
        "message": "Заказ не найден"
    }