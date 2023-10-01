# Тесты на проверку параметра orders при получении заказа по его номеру параметр track в веб- приложении Яндекс Самокат
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
- Файл **configuration.py** (C:\Users\yadsi\PycharmProjects\diplompythonProject\configuration.py) содержит  необходимые ссылки в API Яндекс Самоката
- Файл **data.py** (C:\Users\yadsi\PycharmProjects\diplompythonProject\data.py) содержит тела запросов в формате json
- Файл **sender_stand_request.py** (C:\Users\yadsi\PycharmProjects\diplompythonProject\sender_stand_request.py) содержит импорты пакетов configuration, requests. data и функции для обращения к документации API
- Файл **create_orders_test.py** (C:\Users\yadsi\PycharmProjects\diplompythonProject\create_orders_test.py) содержит импорты пакетов sender_stand_request, data и тесты для проверки передачи заказа созгално  API
- Тест запускается командой Run Test
- 