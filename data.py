class Url:
    URL_MAIN = 'https://qa-scooter.praktikum-services.ru'
    API_COURIER = '/api/v1/courier'
    COURIER_LOGIN = '/api/v1/courier/login'
    API_ORDER = '/api/v1/orders'

    def create_courier():
        return f'{Url.URL_MAIN}{Url.API_COURIER}'
    def delete_courier(courier_id):
        return f'{Url.create_courier()}/{courier_id}'
    def courier_login():
        return f'{Url.URL_MAIN}{Url.COURIER_LOGIN}'
    def order_url():
        return f'{Url.URL_MAIN}{Url.API_ORDER}'
    def order_cancel_url():
        return f'{Url.URL_MAIN}{Url.API_ORDER}/cancel'
    def set_order_to_courier(order_track):
        return f'{Url.URL_MAIN}{Url.API_ORDER}/accept/{order_track}'
    def get_order_id_by_track():
        return f'{Url.URL_MAIN}{Url.API_ORDER}/track'

class Responses:
    OK_TRUE = {'ok': True}
    LOGIN_ALREADY_EXiSTS = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    MISSING_DATA_TO_CREATE = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    ACCOUNT_NOT_FOUND = {"code": 404, "message": "Учетная запись не найдена"}
    MISSING_DATA_TO_LOGIN = {"code": 400, "message": "Недостаточно данных для входа"}
    COURIER_NOT_FOUND = {"code": 404, "message": "Курьера с таким id нет."}
    #    NOT_ENOUGH_DATA_FOR_DELETE = {"message": "Недостаточно данных для удаления курьера"}
    ORDER_NOT_FOUND = {"code": 404, "message": "Заказ не найден"}
    NO_DATA_FOR_SEARCH = {"code": 400, "message": "Недостаточно данных для поиска"}

class TestDataCreateCourier:
    CREATE_COURIER_BODY = {
        "login": "JimmyEatWorld",
        "password": "Qwert!@#$",
        "firstName": "Jim"
    }

class TestDataLogin:
    AUTH_COURIER_BODY = {
        "username": "testUser88",
        "password": "password123"
    }