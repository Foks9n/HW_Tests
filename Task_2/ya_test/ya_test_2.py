import unittest
from Task_2.ya_main.ya_main_2 import login_yandex_from_chrome, login, password

class TestYandexLogin(unittest.TestCase):

    def test_login_yandex_from_chrome(self):
        self.assertTrue(login_yandex_from_chrome(login, password), "Не прошла авторизация электронной почты")
