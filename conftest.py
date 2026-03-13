
import pytest
from django.urls import reverse


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()


@pytest.fixture
def users_data():

   return {
    "password":
        "12345"
    ,
    "email":
        "test11432@test1.ru"

}


@pytest.fixture
def ads_data():

   return {
    "title":
        "Тест"
    ,
    "author":
        "1"

}

@pytest.fixture
def ads_data_update():

   return {
    "title":
        "Тест изменили заголовок"
}

@pytest.fixture
def get_user_token(api_client,users_data):
    url1 = reverse('users:register')
    response1 = api_client.post(url1, data=users_data)
    url = reverse('users:token')
    response = api_client.post(url, data=users_data)

    return response.data.get('access')