# coding=utf-8

import paramiko
# import os

# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )

class SSHConnection(object):
    def __init__(self, host="192.168.12.68", port=22, username="", pwd=None, private_key_file=""):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.private_key = paramiko.RSAKey.from_private_key_file(private_key_file)
        self.__k = None
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd, pkey=self.private_key)
        self.__transport = transport

    def run(self):
        self.upload('db.py', '/tmp/1.py')  # 将本地的db.py文件上传到远端服务器的/tmp/目录下并改名为1.py
        self.cmd('df')  # 执行df 命令
        self.close()  # 关闭连接

    def close(self):
        self.__transport.close()

    def upload(self, local_path, target_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(local_path, target_path)

    def download(self, target_path, local_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.get(target_path, local_path)

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        print(result)
        return result


# ssh = SSHConnection(host="106.75.162.95", port=9007, username="htdev", pwd=None, private_key_file=r"./rebuild_test_htdev")
# local_path = PATH("../../apk/temp.txt")
# remove_path = r"/usr/tmp/test.txt"
# ssh.download(remove_path, local_path)
# ssh.cmd("ls")