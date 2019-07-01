# coding=utf-8
# _author_:cuijs
# date:2019-06-27

from BasePage import Action


class Login(Action):
    """登录页面"""
    def readfile(self, index):
        f = open(path + 'test.txt')
        d = f.readlines()
        f.close()
        return d[index]

    # 选择支付宝账号登录
    tao_button_loc = ('id', '')

    username_loc = ('','')
    pwd_loc = ('','')

    # 登录按钮
    login_button_loc = ('','')
    # 登录后的页面
    login_success_loc = ('','')

    def click_tao_button(self):
        self.click_button(self.tao_button_loc)

    def login_success(self):
        login_success = self.find_element('').text
        self.sssertEaual(login_success, '首页')


if __name__ == '__main__':
    unittest.main()
