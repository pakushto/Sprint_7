import requests
from urls import Urls

class OrderApi:
    @staticmethod
    def create_order(body):
        return requests.post(Urls.CREATE_ORDER_URL, json=body)
    
    @staticmethod
    def get_orders_list(params=None):
        return requests.get(Urls.GET_ORDERS_LIST, params=params)
    
    @staticmethod
    def accept_order(order_id, courier_id):
        return requests.put(Urls.ACCEPT_ORDER_URL.format(order_id=order_id, courier_id=courier_id))
    
    @staticmethod
    def get_order_by_track(track):
        return requests.get(Urls.GET_ORDER_BY_TRACK_URL.format(track=track))  
    
    @staticmethod
    def finish_order(order_id):
        return requests.put(Urls.FINISH_ORDER_URL.format(order_id=order_id))
