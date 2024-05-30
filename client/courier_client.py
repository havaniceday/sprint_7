from client.http_client import HttpClient
from data import Url
import allure


class CourierClient(HttpClient):
    @allure.step("Создание курьера")
    def create_courier(self, courier):
        return self.post(Url.CREATE_COURIER, courier.to_dictionary())

    @allure.step("Логин курьера")
    def login_courier(self, credentials):
        return self.post(Url.COURIER_LOGIN_URL, credentials.__dict__)

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        return self.delete(f'{Url.CREATE_COURIER}/{courier_id}')
