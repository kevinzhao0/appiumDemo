# coding=utf-8

import yaml
import traceback


class DealCase(object):
    def deal_case(self, unittest, driver, path, mylog):
        # for root, subdir, files in os.walk("../yamlcases/"):
        #     for file in files:
        #         file_path = os.path.join(root, file)
        with open(path) as yaml_file:
            data = yaml.load(yaml_file)
            if data is not None:
                for testcase in data["testcases"]:
                    find_type = testcase.get("find_type")
                    action_type = testcase.get("action_type")
                    element_info = testcase.get("element_info")
                    element_index = testcase.get("index")
                    msg = testcase.get("msg")
                    desc = testcase.get("desc")
                    element = self.find_element(driver, element_info, element_index, find_type, desc, mylog)
                    self.action_element(driver, element, action_type, element_index, msg, mylog)
                for check_point in data["checkpoints"]:
                    find_type = check_point.get("find_type")
                    action_type = check_point.get("action_type")
                    element_info = check_point.get("element_info")
                    element_index = check_point.get("index")
                    msg = check_point.get("msg")
                    except_value = check_point.get("except_value")
                    assert_type = check_point.get("assert_type")
                    desc = check_point.get("desc")
                    element = self.find_element(driver, element_info, element_index, find_type, desc, mylog)
                    check_rst = self.check_action(element, action_type, except_value, mylog)
                    self.assert_action(unittest, assert_type, except_value, check_rst)
            else:
                mylog.log_info("请检查用例文件是否存在")

    @staticmethod
    def find_element(driver, element_info, element_index, find_type, desc, mylog):
        # 查找元素
        try:
            mylog.log_info(desc)
            if find_type == "id":
                return driver.find_element_by_id(element_info)
            if find_type == "ids":
                element = driver.find_elements_by_id(element_info)
                if element_index is None:
                    return element
                else:
                    return element[element_index]
            if find_type == "accessibility_id":
                return driver.find_element_by_accessibility_id(element_info)
            if find_type == "class_names":
                element = driver.find_elements_by_class_name(element_info)
                if element_index is None:
                    return element
                else:
                    return element[element_index]
            if find_type == "class_name":
                return driver.find_element_by_class_name(element_info)
            if find_type == "android_uiautomator":
                return driver.find_element_by_android_uiautomator(element_info)
            if find_type == "css_selector":
                return driver.find_element_by_css_selector(element_info)
            if find_type == "xpath":
                return driver.find_element_by_xpath(element_info)
        except Exception, e:
            # mylog.log_info(str(Exception) + str(e))
            mylog.log_info(traceback.format_exc())

    @staticmethod
    def action_element(driver, element, action_type, key_code, msg=None, mylog=None):
        # 动作
        try:
            if action_type == "click":
                element.click()
            if action_type == "send_keys":
                element.clear()
                element.send_keys(msg)
            if action_type == "press_keycode":
                driver.press_keycode(key_code)
            if action_type == "swipe_left":
                width = driver.get_window_size()["width"]
                height = driver.get_window_size()["height"]
                x1 = int(width * 0.75)
                y1 = int(height * 0.5)
                x2 = int(width * 0.05)
                driver.swipe(x1, y1, x2, y1, 600)
            if action_type == "swipe_right":
                width = driver.get_window_size()["width"]
                height = driver.get_window_size()["height"]
                x1 = int(width * 0.05)
                y1 = int(height * 0.5)
                x2 = int(width * 0.75)
                driver.swipe(x1, y1, x2, y1, 600)
            if action_type == "swipe_up":
                width = driver.get_window_size()["width"]
                height = driver.get_window_size()["height"]
                x1 = int(width * 0.5)
                y1 = int(height * 0.75)
                y2 = int(height * 0.05)
                driver.swipe(x1, y1, x1, y2, 600)
            if action_type == "swipe_down":
                width = driver.get_window_size()["width"]
                height = driver.get_window_size()["height"]
                x1 = int(width * 0.5)
                y1 = int(height * 0.05)
                y2 = int(width * 0.75)
                driver.swipe(x1, y1, x1, y2, 600)
        except Exception, e:
            # mylog.log_info(str(Exception) + str(e))
            mylog.log_info(traceback.format_exc())

    @staticmethod
    def check_action(element, action_type, except_value, mylog):
        # 检查动作是否符合预期
        try:
            if action_type == "get_value":
                return element.text
            if action_type == "get_attribute":
                return element.getAttribute("name")
            if action_type == "len_greater":
                return len(element) > except_value
            if action_type == "len_less":
                return len(element) < except_value
            if action_type == "selected":
                return element.is_selected()
        except Exception, e:
            mylog.log_info(traceback.format_exc())

    def assert_action(self, unittest, assert_type, except_value, check_rst):
        # 断言结果与预期一致
        if assert_type == "equal":
            unittest.assertEqual(check_rst, except_value)
        if assert_type == "true":
            unittest.assertTrue(check_rst)
