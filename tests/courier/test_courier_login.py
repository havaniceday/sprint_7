import allure
import pytest
import requests
from client.courier_client import CourierClient
from helper import compose_courier_data
from models.credentials import Credentials
from data import Responses


class TestCourierLogin:
    @allure.title('Логин курьера с корректными данными')
    @allure.description('Тест что курьер может залогиниться успешно.')
    def test_courier_can_log_in_with_correct_data(self, delete_courier):
        courier = compose_courier_data()
        courier_client = CourierClient()
        (data, status_code) = courier_client.create_courier(courier)
        (data, status_code) = courier_client.login_courier(courier)
        assert status_code == requests.codes['ok']
        assert data['id'] is not None
        delete_courier(Credentials(courier.login, courier.password), courier_client)

    @allure.title('Логин курьера с некорректным паролем')
    @allure.description('Тест что курьер не может залогиниться успешно с неверным паролем.')

    def test_courier_can_not_log_in_with_incorrect_pass(self, delete_courier):
        courier = compose_courier_data()
        courier_client = CourierClient()
        (data, status_code) = courier_client.create_courier(courier)
        original_pass = courier.password
        courier.password = "nfhfvgfvgfv"
        (data, status_code) = courier_client.login_courier(courier)
        assert status_code == requests.codes['not_found']
        assert data['message'] == Responses.ACCOUNT_NOT_FOUND['message']
        courier.password = original_pass
        delete_courier(Credentials(courier.login, courier.password), courier_client)

    @allure.title('Логин курьера с пустым паролем')
    @allure.description('Тест что курьер не может залогиниться успешно без пароля.')

    def test_courier_can_not_log_in_with_empty_pass(self, delete_courier):
        courier = compose_courier_data()
        courier_client = CourierClient()
        (data, status_code) = courier_client.create_courier(courier)
        original_pass = courier.password
        courier.password = ""
        (data, status_code) = courier_client.login_courier(courier)
        assert status_code == requests.codes['bad_request']
        assert data['message'] == Responses.MISSING_DATA_TO_LOGIN['message']
        courier.password = original_pass
        delete_courier(Credentials(courier.login, courier.password), courier_client)
    @allure.title('Логин курьера с некорректным логином')
    @allure.description('Тест что курьер не может залогиниться успешно с неверным логином.')
    def test_courier_can_not_log_in_with_incorrect_login(self, delete_courier):
        courier = compose_courier_data()
        courier_client = CourierClient()
        (data, status_code) = courier_client.create_courier(courier)
        original_log = courier.login
        courier.login = "nfhfvgfvgfv"
        (data, status_code) = courier_client.login_courier(courier)
        assert status_code == requests.codes['not_found']
        assert data['message'] == Responses.ACCOUNT_NOT_FOUND['message']
        courier.login = original_log
        delete_courier(Credentials(courier.login, courier.password), courier_client)

    @allure.title('Логин курьера с пустым логином')
    @allure.description('Тест что курьер не может залогиниться успешно без логина.')
    def test_courier_can_not_log_in_with_empty_login(self, delete_courier):
        courier = compose_courier_data()
        courier_client = CourierClient()
        (data, status_code) = courier_client.create_courier(courier)
        original_log = courier.login
        courier.login = ""
        (data, status_code) = courier_client.login_courier(courier)
        assert status_code == requests.codes['bad_request']
        assert data['message'] == Responses.MISSING_DATA_TO_LOGIN['message']
        courier.login = original_log
        delete_courier(Credentials(courier.login, courier.password), courier_client)
