# coding=utf-8

import subprocess
import requests
import re
import requests.exceptions
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AppiumServer(object):
    def start_server(self):
        cmd = "appium --address 127.0.0.1 --port 4723 --session-override"
        start_sub = subprocess.Popen(cmd, shell=True, stdout=open(PATH("../../log/appium.log"), "a"), stderr=subprocess.STDOUT)
        # 等待子进程结束
        start_sub.communicate()

    def get_server_state(self):
        try:
            url = "http://localhost:4723/wd/hub/status"
            response = requests.get(url)
            return response.status_code
        except requests.exceptions.ConnectionError:
            print "the server is not running"

    def stop_server(self):
        cmd_pid = "netstat -ano | findstr 4723"
        pid_result = subprocess.Popen(cmd_pid, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for i in pid_result.stdout.readlines():
            temp = re.findall(r"LISTENING(.*)", i)
            if len(temp)>0:
                pid = temp[0].strip()
                cmd_kill = "taskkill -f -pid " + pid
                subprocess.Popen(cmd_kill, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
