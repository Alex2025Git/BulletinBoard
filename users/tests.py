import pytest
from django.urls import reverse
from users.models import User

@pytest.mark.django_db
def test_unauthorized_request(api_client,users_data):
   url = reverse('users:register')
   response = api_client.post(url,data=users_data)
   user_count = User.objects.count()

   assert user_count == 1
   assert response.status_code == 201

   url2 = reverse('users:token')
   response2 = api_client.post(url2,data=users_data)

   assert response2.status_code == 200
   assert response2.data.get('refresh') != None
