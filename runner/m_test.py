import unittest
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class test(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6'
        desired_caps['deviceName'] = 'MEIZU'
        desired_caps['udid'] = '621QTCQ8222FV'
        # desired_caps['app'] = ''
        desired_caps['appPackage'] = 'com.dolphin.insuranceAgent'
        desired_caps['appActivity'] = '.ui.activity.SplashActivity'
        # desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # desired_caps['deviceReadyTimeout']
        # desired_caps['newCommandTimeout']
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test(self):
        WebDriverWait(driver=self.driver, timeout=10).until(self.driver.find_element_by_id(""))
        ele = self.driver.find_element_by_id("")
        if ele.is_displayed() == True:


