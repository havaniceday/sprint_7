import allure
import requests
from client.order_client import OrderClient
from helper import compose_order_data
from data import OrderData
import pytest


class TestCreateOrder:
    @allure.title('Создание заказа')
    @allure.description('Тест что заказ создается успешно без цветов.')
    def test_create_order_without_colors(self):
        order = compose_order_data()
        order_client = OrderClient()
        (data, status_code) = order_client.create_order(order)
        track = data['track']

        assert status_code == requests.codes['created']
        assert track is not None

        order_client.cancel_order(track)

    @allure.title('Создание заказа c заполением поля цвет 2 цвета')
    @allure.description('Тест что заказ создается успешно c двумя цветами')
    def test_create_order_with_known_colors(self):
        order = compose_order_data()
        order.color = OrderData.AVAILABLE_COLORS
        order_client = OrderClient()
        (data, status_code) = order_client.create_order(order)
        track = data['track']

        assert status_code == requests.codes['created']
        assert track is not None

        order_client.cancel_order(track)


    @pytest.mark.parametrize("color_index", [0, 1])
    @allure.title('Создание заказа c заполением поля цвет 1  цвет')
    @allure.description('Тест что заказ создается успешно c одним цветом')
    def test_create_order_with_one_color(self, color_index):
        order = compose_order_data()
        order.color = [OrderData.AVAILABLE_COLORS[color_index]]
        order_client = OrderClient()
        (data, status_code) = order_client.create_order(order)
        track = data['track']
        assert status_code == requests.codes['created']
        assert track is not None

        order_client.cancel_order(track)
    @allure.title('Создание заказа c не верным заполением поля цвет')
    @allure.description('Тест что заказ создается успешно c двумя не известными цветами')
    def test_create_order_with_invalid_colors(self):
        order = compose_order_data()
        order.color = ['324', 'G234REY']
        order_client = OrderClient()
        (data, status_code) = order_client.create_order(order)
        track = data['track']

        assert status_code == requests.codes['created']
        assert track is not None

        order_client.cancel_order(track)
