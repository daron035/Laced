from django.contrib.auth import get_user_model

import pytest


pytestmark = pytest.mark.django_db


class TestCurrencyEndpoints:
    endpoints = [
        "/api/",
        "/api/auth/users/",
        "/api/auth/jwt/create/",
        "/api/auth/users/me/",
    ]
    user = get_user_model()

    def test_user(self, api_client, user_data):
        response = api_client().get(self.endpoints[0])
        assert response.status_code == 200

    #     response = api_client().post(self.endpoints[1], user_data)
    #     assert response.status_code == 201
    #     assert len(json.loads(response.content)) == 5
    #     assert response.data["first_name"] == "first_name"
    #     assert response.data["role"] == "customer"
    #
    #     # JWT create
    #     customer_user = self.user.objects.first()
    #     assert customer_user.Role.CUSTOMER
    #     assert customer_user.Role.CUSTOMER == "customer"
    #     customer_user.is_active = True
    #     customer_user.save()
    #     response = api_client().post(self.endpoints[2], user_data)
    #     assert len(json.loads(response.content)) == 2
    #     assert response.data["refresh"]
    #     assert response.data["access"]
    #
    #     # Retrieve user
    #     access_token = response.data["access"]
    #     refresh_token = response.data["refresh"]
    #
    #     response = api_client().get(
    #         self.endpoints[3],
    #         headers={"Authorization": f"JWT {access_token}"},
    #     )
    #     assert response.status_code == 200
    #
    #     # post_save
    #     assert customer_user.account
    #     assert not customer_user.account.phone
    #     assert not customer_user.account.balance
    #     assert customer_user.account.balance == None
    #
    #     response = api_client().get(
    #         self.endpoints[3],
    #         headers={"Authorization": f"JWT {refresh_token}"},
    #     )
    #     assert response.status_code == 403
    #
    # def test_admin(self, api_client, admin_data, fail_admin_data):
    #     response = api_client().post(self.endpoints[1], admin_data)
    #     assert response.status_code == 201
    #     assert len(json.loads(response.content)) == 5
    #     assert response.data["role"] == "admin"
    #     admin_user = self.user.objects.first()
    #     assert admin_user.Role.ADMIN
    #     assert admin_user.Role.ADMIN == "admin"
    #
    #     response = api_client().post(self.endpoints[1], fail_admin_data)
    #     assert response.status_code == 400
