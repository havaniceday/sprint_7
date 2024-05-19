from client.http_client import HttpClient
from data import Url


class OrderClient(HttpClient):
    def create_order(self, order):
        return self.post(Url.order_url(), order.to_dictionary())

    def cancel_order(self, track):
        return self.put(Url.order_cancel_url(), {'track': track})

    def get_order_list(self, courier_id):
        return self.get(Url.order_url(), {'courierId': courier_id})

    def set_order_to_courier(self, order_track, courier_id):
        return self.put(Url.set_order_to_courier(order_track), {'courierId': courier_id})

    def get_order_id_by_track(self, order_track):
        return self.get(Url.get_order_id_by_track(), {'t': order_track})
