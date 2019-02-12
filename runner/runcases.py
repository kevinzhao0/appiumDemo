# coding=utf-8

import unittest
import threading
import time
from Base.pre_action.baseADB import BaseAdb
from Base.pre_action.server import AppiumServer
from Base.baseaction.commonutils import CommonUtils
import HTMLTestRunner
import os

appium_server = AppiumServer()
base_adb = BaseAdb()
app_status = CommonUtils()

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# 启动appium服务
def start_server():
    t_stop = threading.Thread(target=appium_server.stop_server)
    t_start = threading.Thread(target=appium_server.start_server)

    t_stop.setDaemon(True)
    t_start.setDaemon(True)

    t_stop.start()
    t_stop.join()

    t_start.start()
    time.sleep(5)

    server_stat = appium_server.get_server_state()
    return server_stat


# 封装suite
def start_test(pattern=""):
    if pattern == "logged*":
        # 确认APP登录状态
        if app_status.login():

        test_dir = PATH("../")
        test_suite = unittest.TestSuite()
        dis_suites = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern=pattern, top_level_dir=None)
        for dis_suite in dis_suites:
            for dis_case in dis_suite:
                test_suite.addTests(dis_case)
        return test_suite
    elif pattern == "nolog*":
        test_dir = PATH("../")
        test_suite = unittest.TestSuite()
        dis_suites = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern=pattern, top_level_dir=None)
        for dis_suite in dis_suites:
            for dis_case in dis_suite:
                test_suite.addTests(dis_case)
        return test_suite
    else:
        print "please check the pattern that you use to discover suite"


if __name__ == "__main__":
    if base_adb.adb_state():
        try:
            if start_server() == 200:
                suite = start_test(pattern="logged*")
                # 获取当前时间
                now = time.strftime("%Y-%m-%d %H_%M_%S")
                # 定义个报告存放路径
                html_report = PATH("../report/"+ now + "result.html")
                fp = file(html_report, 'a')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"APP自动化测试报告", description=u"用例执行情况：")
                runner.run(suite)
            else:
                print "please restart the appium server"
        except Exception, e:
            print e
        finally:
            fp.close()
            appium_server.stop_server()
    else:
        print "请连接设备"