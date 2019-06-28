#_author_:cuijs
#date:2019-06-27
from BasePage import Action
class login(Action):
    """登录页面"""
    # 选择支付宝账号登录
    tao_button_loc = ('id', '')

    username_loc = ('','')
    pwd_loc = ('','')

    # 登录按钮
    login_button_loc = ('','')
    # 登录后的页面
    login_succes_loc = ('','')

    def click_tao_button(self):
        self.click_button(self.tao_button_loc)


if __name__ == '__main__':
    unittest.main()
