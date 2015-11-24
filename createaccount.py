#!/usr/bin/env python
'''\
Usage: ./createaccount

create default ethereum accounts

'''
################################################################################
import subprocess
import socket
import signal
import shutil
import time
import sys
import os
import pexpect


class ImportAccount():

    def __init__(self):
        self.log = sys.stdout
        self.notregistered = True

    def touch(self, fname, times=None):
        with open(fname, 'a'):
           os.utime(fname, times)

    def reguser(self, command):
        argv = command.split(' ')
        child = pexpect.spawn(command)
        if self.notregistered:
           self.notregistered = False
           child.expect('[y/N]')
           child.sendline('y\n')
        child.expect(pexpect.EOF, timeout=None)
        cmd_show_data =  child.before
        cmd_output = cmd_show_data.split('\r\n')
        for data in cmd_output:
            print data

    def reg(self):
        with open("priv_genesis.key") as f:
            for line in f:
               fi = open('temp_pri.key','w')
               fi.write(line) 
               fi.close()
               self.touch("password.txt")
               self.reguser("geth --password password.txt account import temp_pri.key")
               

def main():
    node = ImportAccount()
    node.reg()

if __name__ == '__main__':
    main()
