from client.http_client import HttpClient
from data import Url


class CourierClient(HttpClient):
    def create_courier(self, courier):
        return self.post(Url.create_courier(), courier.to_dictionary())

    def login_courier(self, credentials):
        return self.post(Url.courier_login(), credentials.__dict__)

    def delete_courier(self, courier_id):
        return self.delete(Url.delete_courier(courier_id))
