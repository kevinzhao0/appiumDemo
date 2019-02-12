# coding=utf-8

import unittest
from appium import webdriver
from Base.pre_action.devices import DevicesInfo
from Base.pre_action.baseADB import BaseAdb
from Base.baseaction.baselog import MyLog


def get_device_driver():
    device_info = DevicesInfo()
    b_adb = BaseAdb()
    desired_caps = {}
    desired_caps['app'] = device_info.get_apk_path()
    desired_caps['platformName'] = "Android"
    desired_caps['platformVersion'], desired_caps['deviceName'] = device_info.get_device_info(b_adb)
    desired_caps['udid'] = device_info.get_device_uid(b_adb)
    # desired_caps['appPackage'], desired_caps['appActivity'] = device_info.get_app_info(b_adb)
    # 解决多次切换到webview报错问题，每次切换到非chrome-Driver时kill掉session 注意这个设置在appium 1.5版本上才做了处理
    # desired_caps["recreateChromeDriverSessions"] = "True"
    desired_caps["noReset"] = "True"
    desired_caps['noSign'] = "True"
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver, desired_caps


class UnitTestCase(unittest.TestCase):
    # def __init__(self, methodName='runTest'):
    #     super(UnitTestCase).__init__._testMethodName = methodName

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.driver, cls.desired_caps = get_device_driver()
        cls.driver.implicitly_wait(10)
        cls.my_log = MyLog(cls.desired_caps["deviceName"])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
