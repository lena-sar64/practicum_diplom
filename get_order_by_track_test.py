# Лена Матвеева, 23-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import configuration
import requests
import data


# сохранение track заказа
def get_order_track():
    order_response = sender_stand_request.new_order(data.order_body)
    order_track = order_response.json()["track"]
    track = str(order_track)
    return track


# получение заказа по track
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + track)


# проверка статуса ответа при запросе заказа по track
def test_get_order_by_track():
    test_track = get_order_track()
    response = get_order_by_track(test_track)
    assert response.status_code == 200
