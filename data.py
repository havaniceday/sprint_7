class Url:
    URL_MAIN = 'https://qa-scooter.praktikum-services.ru'
    API_COURIER = '/api/v1/courier'
    COURIER_LOGIN = '/api/v1/courier/login'
    API_ORDER = '/api/v1/orders'
    CREATE_COURIER = f'{URL_MAIN}{API_COURIER}'
    COURIER_LOGIN_URL = f'{URL_MAIN}{COURIER_LOGIN}'
    ORDER_URL = f'{URL_MAIN}{API_ORDER}'
    ORDER_CANCEL_URL = f'{URL_MAIN}{API_ORDER}/cancel'
    GET_ORDER_ID_BY_TRACK = f'{URL_MAIN}{API_ORDER}/track'

class Responses:
    OK_TRUE = {'ok': True}
    LOGIN_ALREADY_EXiSTS = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    MISSING_DATA_TO_CREATE = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    ACCOUNT_NOT_FOUND = {"code": 404, "message": "Учетная запись не найдена"}
    MISSING_DATA_TO_LOGIN = {"code": 400, "message": "Недостаточно данных для входа"}
    COURIER_NOT_FOUND = {"code": 404, "message": "Курьера с таким id нет."}
    ORDER_NOT_FOUND = {"code": 404, "message": "Заказ не найден"}
    NO_DATA_FOR_SEARCH = {"code": 400, "message": "Недостаточно данных для поиска"}


class OrderData:
    AVAILABLE_COLORS = ['BLACK', 'GREY']
