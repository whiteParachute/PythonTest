#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
bd面试题：100个服务器，某文件夹下只有一个文件，检查这个文件大小，大于等于100G时服务器重启
写的时候没搞出来多线程和paramiko丢人了，现在补上

"""

import re
import threading
from time import sleep

import paramiko


class SSHConnection(object):

    def __init__(self, hostname, username, password=None, port=22):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def __del__(self):
        self.close()

    def close(self):
        if self.__transport:
            self.__transport.close()
            self.__transport = None

    def connect(self):
        transport = paramiko.Transport((self.hostname, self.port))
        transport.connect(username=self.username, password=self.password)
        self.__transport = transport

    def execCommand(self, command, timeout=120):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        stdin, stdout, stderr = ssh.exec_command(command, timeout=timeout)
        res = stdout.read()
        error = stderr.read()
        if error.strip():
            return {'color': 'red', 'res': error}
        else:
            return {'color': 'green', 'res': res}


def get_file_size(ip, username, password):
    while True:
        client = SSHConnection(ip, username, password)
        client.connect()
        res = client.execCommand(
            "cd /root && du -h --max-depth=1 | awk 'END {print}'")
        print("ip: " + ip + " size: " + res['res'])
        size = re.findall('(.*)\\t\.\\n', res['res'])
        # print(size)
        if size[0][-1] == "G" and int(size[0][0:-1]) >= 100:
            reb = client.execCommand("ls")
            print("ip: " + ip + " ls: " + reb['res'])
        client.close()
        sleep(3)


def size_loop(host_list):
    thread_list = []
    for ip, username, password in host_list:
        t = threading.Thread(target=get_file_size,
                             args=(ip, username, password))
        thread_list.append(t)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()


ip_pool = [["51.2.190.108", "root", "Huawei123"],
           ["51.2.190.109", "root", "Huawei123"],
           ["51.38.54.124", "root", "Huawei123"]]

size_loop(ip_pool)
