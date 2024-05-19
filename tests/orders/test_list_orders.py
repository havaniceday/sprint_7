import allure
import requests
from client.order_client import OrderClient
from helper import compose_order_data


class TestListOrder:
    @allure.title('Получение заказов')
    @allure.description('Тест что по id курьера получаются заказы')
    def test_get_orders_by_courier_id(self, set_order_to_courier):
        (courier_id, order_track) = set_order_to_courier

        (data, status_code) = OrderClient().get_order_list(courier_id)

        assert requests.codes['ok'] == status_code
        assert data['orders'][0]['track'] == order_track
        assert data['orders'][0]['courierId'] == courier_id
        assert data['pageInfo']['total'] > 0
