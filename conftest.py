import pytest
import allure
from client.courier_client import CourierClient
from client.order_client import OrderClient
from helper import compose_courier_data
from helper import compose_order_data
from models.credentials import Credentials


@pytest.fixture(scope='function')
def delete_courier():
    @allure.step('Удаление курьера')
    def _delete_courier(data, client):
        courier_client = CourierClient()
        (login_response, _) = client.login_courier(data)
        client.delete_courier(login_response['id'])

    return _delete_courier

@pytest.fixture(scope='function')
def delete_order():
    @allure.step('Удаление заказа по треку')
    def _delete_order(track):
        (login_response, _) = OrderClient().cancel_order(track)

    return _delete_order

@pytest.fixture(scope='function')
def set_order_to_courier():
    courier_client = CourierClient()
    order_client = OrderClient()

    courier = compose_courier_data()
    courier_client.create_courier(courier)
    (created_courier, _) = courier_client.login_courier(Credentials(courier.login, courier.password))
    courier_id = created_courier['id']

    order = compose_order_data()
    (created_order, _) = order_client.create_order(order)
    track = created_order['track']

    (order_by_track, _) = order_client.get_order_id_by_track(track)
    order_id = order_by_track['order']['id']

    order_client.set_order_to_courier(order_id, courier_id)

    yield courier_id, track

    order_client.cancel_order(track)
    courier_client.delete_courier(courier_id)
