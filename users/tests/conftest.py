#
# import pytest
# from rest_framework.test import APIClient
#
#
# from users.models import User
# import requests
#
#
# @pytest.fixture
# def register_user():
#     """
#     Фикстура для регистрации пользователя
#     """
#     return User.objects.create(
#         email="test2@test.ru",
#         password="1234",
#     )
#
#
# @pytest.fixture
# def reg_user(password, email):
#     url = "http://127.0.0.1:8000/users/register/"
#     data = {"email": "test2@test.ru", "password": "1234"}
#     response = requests.post(url, json=data)
#     return response.json()
#
#
# @pytest.fixture(autouse=True)
# def api_client():
#     """
#     Фикстура для создания экземпляра тестового API-клиента
#     """
#
#     return APIClient()

