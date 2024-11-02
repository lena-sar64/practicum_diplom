import configuration
import requests


# создание нового заказа
def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER_PATH,
                         json=body)
