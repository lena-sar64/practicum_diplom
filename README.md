# Тест на проверку получения заказа по его track для Яндекс Самокат
- Для запуска теста должны быть установлены пакеты pytest и requests
- Запуск теста выполянется командой pytest
- Нужно запустить сервер url.serverhub.praktikum-services.ru и указать путь в файле configuration.py

# Эндпоинт для создания нового заказа 
POST /api/v1/orders - путь указан в файле configuration.py, набор данных для создания заказа 
(order_body) указан в файле data.py

# Эндпоинт для получения заказа по track
GET /api/v1/orders/track - путь указан в файле configuration.py

# Функции:
- для создания нового заказа написана в файле sender_stand_request.py
- для сохранения track и получения заказа по нему написаны в файле get_order_by_track_test.py
- также в файле get_order_by_track_test.py написана тестовая функция test_get_order_by_track, проверяющая код ответа на запрос по получению заказа по track
