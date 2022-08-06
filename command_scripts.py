#!/usr/bin/env python3
import sys
sys.path.insert(0, "/opt/ametr")
import subprocess
import os
import time

import dbSqliteAlpameter as db
import brom_add_inventory_1c
import printQR
from datetime import datetime
#import camera_remote

def video_on():
    cmd = '/opt/ametr/alpanometer.sh'
    subprocess.Popen(cmd, shell=True)
    return  0

def video_off():
    os.system('reboot now')
    return  0

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

def save_to_1c():
    last_doc_number = int(db.get_last_doc_number())
    #print(last_doc_number)
    #cur_sc = db.get_last_scanedQR_for_1c(last_doc_number)
    cur_sc = db.doc_for_1c()
    #print(cur_sc)
    bc = ''
    f_ok = False
    for sc in cur_sc:
        bc += sc.part_number
        bc += ';'
        f_ok = True
    if f_ok:
        try:
            #bc = "1002740326155";
            #bc += ";"
            #bc += "2300000060160";
            #print(bc)
            doc_num = brom_add_inventory_1c.create_infentory_1C(bc)
            #doc_num = 'yguguygu'
            db.set_log('Last saved doc to 1c number is ' + doc_num)
            last_doc_number += 1
            db.set_last_doc_number(last_doc_number)
            db.doc_clear_all()
            #print(doc_num)
            return  0
        except:
            #print("not save to 1c")
            db.set_log('Error to  saved doc to 1c')
            return  1
    else:
        db.set_log('Not doc to save to 1c')
        return  1

def focus_on_off():
    db.set_log('Seting focus')
   # camera_remote.set_autofocus("on")
   # time.sleep(7)
   # camera_remote.set_autofocus("off")
   # db.set_log('Focus is OK')

if __name__ == "__main__":
    Bc = "1002740326155";
    Bc += ";"
    Bc += "2300000060160";
    #print(Bc)
    #save_to_1c()
    reprint()
    #video_off()
    #focus_on_off()
