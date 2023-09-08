import configuration
import requests
import data


# создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)


response = post_new_order(data.order_body)
print(response.status_code)


# поиск заказа по трек номеру
def get_order_search(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_TRACK_PATH + str(track))
