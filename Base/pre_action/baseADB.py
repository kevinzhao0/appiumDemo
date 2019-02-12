# coding=utf-8

import subprocess


class BaseAdb(object):
    def __init__(self):
        pass

    def adb_deal_cmd(self, cmd):
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result

    # 获取连接状态
    def adb_state(self):
        state = self.adb_deal_cmd("adb get-state")
        if len(state.stderr.readlines()):
            return 0
        else:
            return 1