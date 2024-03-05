import time
from unittest import TestCase

import requests_mock

from cfc.auth import TOKEN_ISSUER, TOKEN_URL_EXTENSION, authenticate_keycloak


class TestAuth(TestCase):
    @requests_mock.Mocker()
    def test_authenticate_keycloak(self, mock_request: requests_mock.Mocker):
        mock_request.post(
            TOKEN_ISSUER + TOKEN_URL_EXTENSION,
            json={"access_token": "some_access_token", "expires_in": 100},
        )
        token, valid_until = authenticate_keycloak("client_id", "client_secret")

        self.assertEqual("some_access_token", token)
        self.assertAlmostEqual(time.time() + 100, valid_until, delta=5)
