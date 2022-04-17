import unittest

from src.mypythonanywhere import AccountType, FriendlyPythonAnywhereClient

from helpers import load_account_details_from_env


class DefaultPythonTest(unittest.TestCase):

    def setUp(self) -> None:
        (username, token, account_type) = load_account_details_from_env()

        self.client = FriendlyPythonAnywhereClient(
            username=username,
            token=token,
            account_type=AccountType(account_type)
        )

    def test_set_and_get_default_python3_version(self):
        py3_default = self.client.default_python.set_default_python3('3.7')
        py3_default = self.client.default_python.get_default_python3()
        self.assertEqual(py3_default.default_version, '3.7')

    def test_set_and_get_default_python_version(self):
        py_default = self.client.default_python.set_default_python('2.7')
        py_default = self.client.default_python.get_default_python()
        self.assertEqual(py_default.default_version, '2.7')

    def test_set_and_get_save_and_run_default_python(self):
        py_default = self.client.default_python.set_save_and_run_default_python(
            '3.9')
        py_default = self.client.default_python.get_save_and_run_default_python()
        self.assertEqual(py_default.default_version, '3.9')


if __name__ == '__main__':
    unittest.main()
