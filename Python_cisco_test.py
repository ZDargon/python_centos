#! /usr/bin/python
# -*- coding-utf-8 -*-


import paramiko
import time
import getpass

username = input("username: ")
password = getpass.getpass('password: ')
ip = '192.168.199.131'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip,username=username,password=password,look_for_keys=False)

print("Sucessful connect to " + ip)

command = ssh_client.invoke_shell()

command.send("conf t\n")
command.send("do sh ip int b \n")
time.sleep(1)

output = command.recv(65535)

print(output)

ssh_client.close


if __name__ == '__main__':
    pass
