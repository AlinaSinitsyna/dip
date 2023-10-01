import configuration
import requests
import data


def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers) # а здесь заголовки


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_ORDERS_TRAK_PATH + '?t=' + str(track), headers=data.headers)
