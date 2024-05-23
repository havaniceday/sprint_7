from client.http_client import HttpClient
from data import Url
import allure


class OrderClient(HttpClient):
    @allure.step("Создание заказа")
    def create_order(self, order):
        return self.post(Url.ORDER_URL, order.to_dictionary())

    @allure.step("Отмена заказа")
    def cancel_order(self, track):
        return self.put(Url.ORDER_CANCEL_URL, {'track': track})

    @allure.step("Получение списка заказов по ID курьера")
    def get_order_list(self, courier_id):
        return self.get(Url.ORDER_URL, {'courierId': courier_id})

    @allure.step("Назначение курьера на выполнение заказа")
    def set_order_to_courier(self, order_track, courier_id):
        return self.put(f'{Url.URL_MAIN}{Url.API_ORDER}/accept/{order_track}',
                        {'courierId': courier_id})

    @allure.step("Получение ID заказа по треку")
    def get_order_id_by_track(self, order_track):
        return self.get(Url.GET_ORDER_ID_BY_TRACK, {'t': order_track})
