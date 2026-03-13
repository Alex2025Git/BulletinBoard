import pytest
from django.urls import reverse
from ads.models import Ads

@pytest.mark.django_db
def test_create_update_ads(api_client,ads_data,get_user_token,ads_data_update):
   url_create = reverse('ads:ads_create')
   response_create = api_client.post(url_create,data=ads_data, HTTP_AUTHORIZATION=f"Bearer {get_user_token}")
   ads_count = Ads.objects.count()

   assert ads_count == 1
   assert response_create.status_code == 201

   url_update = reverse('ads:ads_update', kwargs={'pk': 1})
   response_update = api_client.put(url_update,data=ads_data_update, HTTP_AUTHORIZATION=f"Bearer {get_user_token}")

   assert response_update.status_code == 200

   ads_get = Ads.objects.get(pk=1)
   assert ads_get.title == ads_data_update['title']