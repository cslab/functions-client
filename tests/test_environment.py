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

        # test special characters in values
        env_var_callback("VAR1=p@ssw0rd!")
        env_var_callback("VAR1=value#1")
        env_var_callback("VAR1=hello!,VAR2=world?")
        env_var_callback("SECRET=abc$def%ghi^jkl&mno*pqr")

        # test invalid input
        with self.assertRaises(typer.BadParameter):
            env_var_callback("VAR1=VALUE1,VAR2=VALUE2,")
        with self.assertRaises(typer.BadParameter):
            env_var_callback("VAR1=VALUE1,VAR2=VALUE2,VAR3")
        with self.assertRaises(typer.BadParameter):
            env_var_callback("VAR1=VALUE1,VAR2=VALUE2,VAR3=VALUE3=")
        with self.assertRaises(typer.BadParameter):
            env_var_callback("VAR1=value with spaces")
        with self.assertRaises(typer.BadParameter):
            env_var_callback("VAR1=val1,VAR2=val=2")
