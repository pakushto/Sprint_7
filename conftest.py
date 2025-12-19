import pytest
from api.courier_api import CourierApi
from api.order_api import OrderApi
from helper import CourierFactory, OrderFactory


@pytest.fixture(scope="function")
def courier_body():
    """Генерирует тело курьера со случайными данными."""
    return CourierFactory.default_body_with_random_parameters()

@pytest.fixture(scope='function')
def cleanup_courier():
    courier_ids = []
    yield courier_ids
    for courier_id in courier_ids:
        CourierApi.delete_courier(courier_id=courier_id)

@pytest.fixture(scope='function')
def login_courier(courier_body):
    return CourierApi.login_courier(courier_body)

@pytest.fixture(scope='function')
def create_courier(courier_body):
    body = courier_body
    response = CourierApi.create_courier(courier_body)
    return {
        "body": body,
        "response": response
    }

@pytest.fixture(scope='function')
def create_and_login_courier(courier_body):
    CourierApi.create_courier(courier_body)
    response = CourierApi.login_courier(courier_body)
    courier_id = response.json()["id"]
    
    yield {
        "response": response,
        "body": courier_body,
        "id": courier_id
    }

    CourierApi.delete_courier(courier_id)

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

