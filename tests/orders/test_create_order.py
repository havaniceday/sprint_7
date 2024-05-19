import allure
import requests
from client.order_client import OrderClient
from helper import compose_order_data


class TestCreateOrder:
    @allure.title('Создание заказа')
    @allure.description('Тест что заказ создается успешно без цветов.')
    def test_create_order_without_colors(self):
        order = compose_order_data()
        (data, status_code) = OrderClient().create_order(order)
        track = data['track']

        assert status_code == requests.codes['created']
        assert track is not None

        OrderClient().cancel_order(track)

    @allure.title('Создание заказа c заполением поля цвет')
    @allure.description('Тест что заказ создается успешно c двумя цветами')
    def test_create_order_with_known_colors(self):
        order = compose_order_data()
        order.color = ['BLACK', 'GREY']
        (data, status_code) = OrderClient().create_order(order)
        track = data['track']

        assert status_code == requests.codes['created']
        assert track is not None

        OrderClient().cancel_order(track)

    @allure.title('Создание заказа c не верным заполением поля цвет')
    @allure.description('Тест что заказ создается успешно c двумя не известными цветами')
    def test_create_order_with_invalid_colors(self):
        order = compose_order_data()
        order.color = ['324', 'G234REY']
        (data, status_code) = OrderClient().create_order(order)
        track = data['track']

        assert status_code == requests.codes['created']
        assert track is not None

        OrderClient().cancel_order(track)