#!/usr/bin/env python3
# Author ID: omelnic

import os

def freespace():
    output = os.popen("df -h | grep '/$' | awk '{print $4}'")
    output = output[0].decode('utf-8').strip()
    return output


if __name__ == '__main__':
    print(freespace())