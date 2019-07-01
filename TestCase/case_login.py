# coding=utf-8
# _author_:cuijs
# date:2019-07-01

import unittest
from Page import LoginPage


class CaseLogin(LoginPage.login, unittest.TestCase):
    def test1_login_success(self):
        """正常登录"""
        self.click_tao_button()
        self.assertTrue(self.login_success())


if __name__ == '__main__':
    unittest.main()