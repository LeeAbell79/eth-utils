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

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

def sh(command):
    argv = command.split(' ')
    p = subprocess.Popen(argv,stdin=subprocess.PIPE,stdout=sys.stdout,stderr=sys.stderr)
    p.stdin.close()
    p.wait()
    return 

class ImportAccount():

    def __init__(self):
        self.log = sys.stdout


    def reg(self):
        with open("priv_genesis.key") as f:
            for line in f:
               fi = open('temp_pri.key','w')
               fi.write(line) 
               fi.close()
               touch("password.txt")
               outp = sh("geth --password password.txt account import temp_pri.key")


def main():
    node = ImportAccount()
    node.reg()

if __name__ == '__main__':
    main()
