import os
import time
from unittest import TestCase, mock

from cfc.config import Config


class TestConfig(TestCase):
    def test_save_and_load(self):
        """
        Test that saving and loading the config works
        """
        config1 = Config("tests")
        config1.client_id = "testing_client_id"
        config1.save()

        config2 = Config("tests")
        self.assertEqual("testing_client_id", config2.client_id)

        # clean up
        os.remove(config2.config_path)

    def test_configdir(self):
        """
        Test that a config directory is set automatically
        """

        config = Config()
        self.assertTrue(len(str(config.config_path)) > 0)

    @mock.patch("cfc.config.authenticate_keycloak")
    def test_access_token(self, mock_authenticate):
        config = Config("tests")
        config.client_id = "client"
        config.client_secret = "aaaa"  # nosec
        mock_authenticate.return_value = ("123", time.time() + 100)

        token = config.access_token
        self.assertEqual("123", token)
        mock_authenticate.assert_called_once()

        config2 = Config("tests")
        # make a second call
        token = config2.access_token
        self.assertEqual("123", token)
        # no additional call to authenticate, because it was taken from cache
        mock_authenticate.assert_called_once()

        # clean up
        os.remove(config.config_path)
