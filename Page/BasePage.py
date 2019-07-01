# coding=utf-8
# _author_:cuijs
# date:2019-06-27
import unittest


class Action(unittest.TestCase):
    """
    Base封装公共方法。drive、caps
    """
    def setUp(self):
        print ("--------------开始执行用例------------------6")

    def tearDown(self):
        print("--------------用例执行结束-----------------")

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '4695e5887d14',
            'platformVersion': '6.0',
            # apk包名
            'appPackage': 'com.wondershare.drfone',
            # apk的launcherActivity
            'appActivity': 'com.wondershare.drfone.ui.activity.Main2Activity',
            'noReset': 'false'
        }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDownClass(self):
        cls.driver.quit()

    def find_element(self, loc):
        try:
            webDriverWait(self.driver, 15).until(lambda driver:
                                                 driver.find_element(*loc).is_displaued())
            return self.driver.find_element(*loc)
        except:
            print("%s页面中未能找到%s元素"%(self, loc))

    def clear_keys(self, loc):
        # 重写清空输入框
        time.sleep(1)
        self.find_element(loc).clear()

    def send_keys(self, loc ,value):
        # 重写输入框输入内容
        self.clear_keys(loc)
        self.find_element(loc).send_keys(value)

    def click_button(self, loc):
        # 重写点击按钮
        self.find_element(loc).click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
