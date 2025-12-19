import pytest
from api.courier_api import CourierApi
from api.order_api import OrderApi
from helper import CourierFactory, OrderFactory


@pytest.fixture(scope='function')
def create_courier():
    def _create(body):
        return CourierApi.create_courier(body)
    return _create

@pytest.fixture(scope='function')
def login_courier():
    def _login(body):
        return CourierApi.login_courier({
            "login": body["login"],
            "password": body["password"]
        })
    return _login

@pytest.fixture(scope='function')
def create_and_login_courier(create_courier, login_courier):
    body = CourierFactory.default_body_with_random_parameters()
    create_response = create_courier(body)
    login_response = login_courier(body)
    courier_id = login_response.json().get("id")
    return {
        "id": courier_id,
        "body": body,
        "create_response": create_response,
        "login_response": login_response
    }

@pytest.fixture(scope='function')
def cleanup_courier():
    courier_ids = []
    yield courier_ids
    for courier_id in courier_ids:
        CourierApi.delete_courier(courier_id=courier_id)

@pytest.fixture(scope='function')
def create_order():
    response = OrderApi.create_order(OrderFactory.default_body_with_random_parameters())
    track = response.json()["track"]
    return {
        "response": response,
        "track": track,
    }

@pytest.fixture(scope='function')
def get_order_by_track(create_order):
    response = OrderApi.get_order_by_track(create_order["track"])
    order_id = response.json()["order"]["id"]
    yield {
        "response": response,
        "order_id": order_id,
    }
    OrderApi.finish_order(order_id=order_id)

@pytest.fixture(scope='function')
def finish_order():
    orders = []
    yield orders
    for order in orders:
        OrderApi.finish_order(order)

@pytest.fixture(scope='function')
def finish_order_by_track():
    tracks = []
    yield tracks
    for track in tracks:
        response = OrderApi.get_order_by_track(track=track)
        OrderApi.finish_order(response.json()["order"]["id"])

