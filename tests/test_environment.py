from unittest import TestCase

import typer

from cfc.environment import env_var_callback


class TestEnvironment(TestCase):
    def test_env_var_callback(self):
        # Test valid input
        env_var_callback("VAR1=VALUE1,VAR2=VALUE2")
        env_var_callback("VAR1=abc-123:as123")
        env_var_callback("VAR1=abc-123:as123,VAR2=abc-123:as123")
        env_var_callback("VAR1=https://example.com,VAR2=abc-123:as123")

        # test empty input
        env_var_callback("")

        # test invalid input
        with self.assertRaises(typer.BadParameter):
            env_var_callback("VAR1=VALUE1,VAR2=VALUE2,")
        with self.assertRaises(typer.BadParameter):
            env_var_callback("VAR1=VALUE1,VAR2=VALUE2,VAR3")
        with self.assertRaises(typer.BadParameter):
            env_var_callback("VAR1=VALUE1,VAR2=VALUE2,VAR3=VALUE3=")
