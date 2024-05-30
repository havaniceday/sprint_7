import requests
import random
import string
from models.courier import Courier
from models.order import Order


def compose_courier_data(without_unnecessary_fields=False):
    login = generate_string(10)
    password = generate_string(10)
    first_name = ''
    if not without_unnecessary_fields:
        first_name = generate_string(10)
    return Courier(login, password, first_name)


def compose_order_data():
    first_name = generate_string(5)
    last_name = generate_string(5)
    address = generate_string(25)
    metro_station = random.randint(1, 237)
    phone = f"{random.randint(10000000000, 99999999999)}"
    rent_time = random.randint(1, 7)
    delivery_date = f'2024-{random.randint(1, 12)}-{random.randint(1, 28)}'
    comment = generate_string(10)
    color = []
    return Order(first_name,
                 last_name,
                 address,
                 metro_station,
                 phone,
                 rent_time,
                 delivery_date,
                 comment,
                 color)


def generate_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
