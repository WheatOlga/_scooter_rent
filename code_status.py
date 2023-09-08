import data
import sender_stand_request


# тест на проверку кода ответа (200)
def test_code_200():
    track = sender_stand_request.post_new_order(data.order_body).json()['track']
    response = sender_stand_request.get_order_search(track)
    assert response.status_code == 200

# Ольга Пономарева, 8-я когорта — Финальный проект. Инженер по тестированию плюс