# coding=utf-8

from dealcases.dealcase import DealCase
import os
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

deal_case = DealCase()
yaml_path = PATH("../yamlcases/logged/htcoin_alipay.yaml")


class CommonUtils(object):
    def __init__(self, driver):
        self.driver = driver

    def skip_update(self):
        """跳过更新"""
        btn_next = self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/update_dialog_later")
        if btn_next.is_displayed() == True:
            btn_next.click()

    def skip_lead_page(self):
        """跳过首次引导"""
        pic_lead_page = self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/share_lead_iv")
        if pic_lead_page.is_displayed == True:
            pic_lead_page.click()
            pic_lead_page2 = self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/news_detail_lead_ll")
            pic_lead_page2.click()

    def login(self):
        # 点击我的
        self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/ll_my").click()
        # 点击注册/登陆
        self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/my_login_btn").click()
        # 输入手机号，自动获取验证码并点击登陆
        phone = self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/et_phone")
        phone.clear()
        phone.send_keys("15144445555")
        self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/tv_get_sms").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/btn_ensure").click()
        time.sleep(3)

    def logout(self):
        # 点击我的
        self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/ll_my").click()
        # 点击设置
        self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/iv_system_setting_img").click()
        # 点击退出登录
        self.driver.find_element_by_id("com.dolphin.insuranceAgent:id/btn_exit").click()



