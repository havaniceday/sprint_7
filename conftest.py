import pytest

from client.courier_client import CourierClient
from client.order_client import OrderClient
from helper import compose_courier_data
from helper import compose_order_data
from models.credentials import Credentials


@pytest.fixture(scope='function')
def delete_courier():
    def _delete_courier(data):
        (login_response, _) = CourierClient().login_courier(data)
        CourierClient().delete_courier(login_response['id'])

    return _delete_courier

@pytest.fixture(scope='function')
def delete_order():
    def _delete_order(track):
        (login_response, _) = OrderClient().cancel_order(track)

    return _delete_order

@pytest.fixture(scope='function')
def set_order_to_courier():
    courier = compose_courier_data()
    CourierClient().create_courier(courier)
    (created_courier, _) = CourierClient().login_courier(Credentials(courier.login, courier.password))
    courier_id = created_courier['id']

    order = compose_order_data()
    (created_order, _) = OrderClient().create_order(order)
    track = created_order['track']

    (order_by_track, _) = OrderClient().get_order_id_by_track(track)
    order_id = order_by_track['order']['id']

    OrderClient().set_order_to_courier(order_id, courier_id)

    yield courier_id, track

    OrderClient().cancel_order(track)
    CourierClient().delete_courier(courier_id)
