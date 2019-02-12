# coding=utf-8

import os
import re

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class DevicesInfo(object):
    def __init__(self):
        self.device_udid = ""
        self.platformVersion = ""
        self.deviceName = ""
        self.abs_apk_path = ""

    # 获取设备的UDID
    def get_device_uid(self, b_adb):
        # temp = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE).stdout.readlines()
        cmd = "adb devices"
        temp = b_adb.adb_deal_cmd(cmd).stdout.readlines()
        for i in temp:
            if "device" in i:
                self.device_udid = i.split("\tdevice")[0]
        return self.device_udid

    # 获取设备的名称和设备系统的版本号
    def get_device_info(self, b_adb):
        cmd = "adb shell cat /system/build.prop"
        temp = b_adb.adb_deal_cmd(cmd)
        (out, err) = temp.communicate()
        self.platformVersion = re.findall(r"ro.build.version.release=(.*)", out)[0].strip()
        self.deviceName = re.findall(r"ro.product.name=(.*)", out)[0].strip()
        return self.platformVersion, self.deviceName

    # 获取APK所在路径
    def get_apk_path(self):
        # temp = os.path.abspath("../../apk")
        temp = PATH("../../apk/")
        for file in os.listdir(temp):
            if file.endswith("apk"):
                self.abs_apk_path = os.path.join(temp, file)
                return self.abs_apk_path

    # 获取APP的包名和活动名
    def get_app_info(self, b_adb):
        if len(self.abs_apk_path) == 0:
            self.abs_apk_path = self.get_apk_path()
        cmd = "aapt dump badging " + self.abs_apk_path
        temp = b_adb.adb_deal_cmd(cmd)
        (app_info_output, app_info_err) = temp.communicate()
        package_name = re.findall(r"package: name='(.*)' versionCode", app_info_output)[0]
        activity_name = re.findall(r"launchable-activity: name='(.*)'  label", app_info_output)[0]
        return package_name, activity_name

    # 封装desired_caps
    def get_desired_caps(self, base_adb):
        desired_caps = {}
        desired_caps['app'] = self.get_apk_path()
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'], desired_caps['deviceName'] = self.get_device_info(base_adb)
        desired_caps['udid'] = self.get_device_uid(base_adb)
        desired_caps['appPackage'], desired_caps['appActivity'] = self.get_app_info(base_adb)
        return desired_caps

# if __name__ == "__main__":
#     device_info = DevicesInfo()
#     b_adb = BaseAdb()
#     desired_caps={}
#     desired_caps['app'] = device_info.get_apk_path()
#     desired_caps['platformName'] = "Android"
#     desired_caps['platformVersion'], desired_caps['deviceName'] = device_info.get_device_info(b_adb)
#     desired_caps['udid'] = device_info.get_device_uid(b_adb)
#     desired_caps['appPackage'], desired_caps['appActivity'] = device_info.get_app_info(b_adb)
#     print desired_caps