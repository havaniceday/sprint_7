# sprint_7 

Спринт 7 "Тестирование API"

Проект содержит тесты для API учебного сервиса Яндекс Самокат https://qa-scooter.praktikum-services.ru/.
Ссылка на документацию: https://qa-scooter.praktikum-services.ru/docs/.

Установка библиотек -  pip install -r requirements.txt
Запуcк тестов c генерацией отчетов pytest -vs --alluredir=allure_results
Генерация веб-страницы с тестовыми отчетами allure serve allure_results

Тестируемые эндпоинты:
POST /api/v1/courier - создание курьера test_create_courier.py
POST /api/v1/orders - создание заказа test_create_order.py
POST /api/v1/courier/login - авторизация курьера test_courier_login.py
GET /api/v1/orders - получение списка заказов test_list_orders.py

Тестовое покрытие:

1. Создание курьера test_create_courier.py

курьера можно создать; test_create_courier test_can_create_courier_without_unnecessary_props
нельзя создать двух одинаковых курьеров; test_can_not_create_duplicate_courier
чтобы создать курьера, нужно передать в ручку все обязательные поля; 
запрос возвращает правильный код ответа;
успешный запрос возвращает {"ok":true};
если одного из полей нет, запрос возвращает ошибку; test_can_not_create_courier_without_login test_can_not_create_courier_without_password
если создать пользователя с логином, который уже есть, возвращается ошибка.


2. Логин курьера test_courier_login.py

курьер может авторизоваться; test_courier_can_log_in_with_correct_data
для авторизации нужно передать все обязательные поля; test_courier_can_not_log_in_with_empty_pass test_courier_can_not_log_in_with_empty_login
система вернёт ошибку, если неправильно указать логин или пароль; test_courier_can_not_log_in_with_incorrect_pass test_courier_can_not_log_in_with_incorrect_login
если какого-то поля нет, запрос возвращает ошибку;
если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
успешный запрос возвращает id.



3. Создание заказа test_create_order.py

можно указать один из цветов — BLACK или GREY; test_create_order_with_one_color
можно указать оба цвета; test_create_order_with_known_colors
можно совсем не указывать цвет; test_create_order_without_colors
тело ответа содержит track.

NB! test_create_order_with_invalid_colors - успешно создается ордер с рандомным набором букв вместо цветов


4. Список заказов  test_list_orders.py
Проверь, что в тело ответа возвращается список заказов. test_get_orders_by_courier_id

