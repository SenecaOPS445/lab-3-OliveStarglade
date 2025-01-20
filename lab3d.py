#!/usr/bin/env python3
'''Lab3d Free space on root function'''
# Author ID: omelnic

import subprocess

def free_space():
    # creates subproccess to get available space on the / directory
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    fspace = p.communicate()
    # Convert stdout to a string and strip off the newline characters
    output = fspace[0].decode('utf-8').strip()
    return output


if __name__ == '__main__':
    print(free_space())