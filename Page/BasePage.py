#_author_:cuijs
#date:2019-06-27
import unittest
class Action(unittest.TestCase):
    """
    Base封装公共方法。drive、caps
    """
    def setUp(self):
        print ("--------------开始执行用例------------------6")

    def tearDown(self):
        print ("--------------用例执行结束-----------------")
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
if __name__ == '__main__':
    unittest.main(verbosity=2)


