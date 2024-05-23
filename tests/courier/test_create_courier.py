import allure
import requests
from client.courier_client import CourierClient
from helper import compose_courier_data
from models.credentials import Credentials
from data import Responses


class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Тест что курьер создается успешно.')
    def test_create_courier(self, delete_courier):
        courier = compose_courier_data()
        courier_client = CourierClient()
        (data, status_code) = courier_client.create_courier(courier)

        assert status_code == requests.codes['created']
        assert data['ok'] == True

        delete_courier(Credentials(courier.login, courier.password), courier_client)

    @allure.title('Создание курьера с тем же логином')
    @allure.description('Тест что курьер не будет создан.')
    def test_can_not_create_duplicate_courier(self, delete_courier):
        courier = compose_courier_data()
        courier_client = CourierClient()
        (data1, status_code1) = courier_client.create_courier(courier)
        (data2, status_code2) = courier_client.create_courier(courier)

        assert status_code1 == requests.codes['created']
        assert data1['ok'] == True
        assert status_code2 == requests.codes['conflict']
        assert data2['message'] == Responses.LOGIN_ALREADY_EXiSTS['message']

        delete_courier(Credentials(courier.login, courier.password), courier_client)

    @allure.title('Создание курьера без логина')
    @allure.description('Тест что курьер не будет создан без передачи логина.')
    def test_can_not_create_courier_without_login(self):
        courier = compose_courier_data()
        courier.login = ""

        (data, status_code) = CourierClient().create_courier(courier)

        assert status_code == requests.codes['bad_request']
        assert data['message'] == Responses.MISSING_DATA_TO_CREATE['message']

    @allure.title('Создание курьера без пароля')
    @allure.description('Тест что курьер не будет создан без передачи пароля.')
    def test_can_not_create_courier_without_password(self):
        courier = compose_courier_data()
        courier.password = ""

        (data, status_code) = CourierClient().create_courier(courier)

        assert status_code == requests.codes['bad_request']
        assert data['message'] == Responses.MISSING_DATA_TO_CREATE['message']

    @allure.title('Создание курьера без необязательных полей')
    @allure.description('Тест что курьер будет создан без передачи не обязательных полей')
    def test_can_create_courier_without_unnecessary_props(self, delete_courier):
        courier = compose_courier_data(True)
        courier_client = CourierClient()
        (data, status_code) = courier_client.create_courier(courier)

        assert status_code == requests.codes['created']
        assert data['ok'] == True

        delete_courier(Credentials(courier.login, courier.password), courier_client)
