#!/usr/bin/env python3
import sys
sys.path.insert(0, "/opt/ametr")
import subprocess
import os
import time

import dbSqliteAlpameter as db
#import brom_add_inventory_1c
import printQR
from datetime import datetime
#import camera_remote

def reprint():
    printQR.reprint()

def print_serial(quantity):
    tap_last = db.get_taped()
    name = tap_last.name
    iner_diam = tap_last.iner_diam
    out_diam  = tap_last.out_diam
    epoch32 = datetime.now().timestamp()
    cmd = 'python3 printQR.py'
    cmd += '  --name="' + str(name) + '"'
    cmd += '  --iner=' + str(iner_diam)
    cmd += '  --outer=' + str(out_diam)
    cmd += '  --epoch32=' + str(epoch32)
    cmd += '  --quantity=' + str(quantity)
    print(cmd)
    subprocess.Popen(cmd, shell=True)

def print_clone(qr_array):
    #p_name, p_diam, p_partnum
    name = qr_array[0]
    iner_diam = qr_array[1]
    out_diam  = qr_array[2]
    epoch32 = datetime.now().timestamp()
    cmd = 'python3 printQR.py'
    cmd += '  --name="' + str(name) + '"'
    cmd += '  --iner="' + str(iner_diam) + '"'
    cmd += '  --outer="' + str(out_diam) + '"'
    cmd += '  --epoch32=' + str(epoch32)
    cmd += '  --quantity=1'
    cmd += '  --clone=1'
    print(cmd)
    subprocess.Popen(cmd, shell=True)


if __name__ == "__main__":
    Bc = "1002740326155";
    Bc += ";"
    Bc += "2300000060160";
    #print(Bc)
    #save_to_1c()
    reprint()
    #video_off()
    #focus_on_off()
