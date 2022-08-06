#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import sys
import serial
import time  # Optional (required if using time.sleep() below)
import dbSqliteAlpameter as db
import command_scripts


def main_scan():
    # Use a breakpoint in the code line below to debug your script.
    port = '/dev/ttyACM0'
    baud = 9600
    ser = serial.Serial(port, baud, timeout=0)
    print("connected to: " + ser.portstr)

    while (True):
        # NB: for PySerial v3.0 or later, use property `in_waiting` instead of
        # function `inWaiting()` below!
        if (ser.inWaiting() > 0):  # if incoming bytes are waiting to be read from
            # the serial input buffer
            # read the bytes and convert from binary array to ASCII
            data_str = ser.read(ser.inWaiting())
            try:
                data_str = data_str.decode('ascii')
                # print the incoming string without putting a new-line
                # ('\n') automatically after every print()
                #print(data_str, end='')
                #data_str = ser.readline().decode('ascii')
                print(data_str)
                # in_array = data_str.split('\n')
                # print(in_array)
                qr_str = []
                line_count = 0
                line = ''
                for c in data_str:
                    if c == '\n':
                        print("Line: " + ''.join(line))
                        qr_str.append(line)
                        line = ""
                        line_count += 1
                        # break
                    elif c == '\r':
                        pass
                    else:
                        line += c

                print(qr_str)
                clone = db.get_clone()
                if clone == 0:
                    if len(qr_str[0]) >= 3 \
                            and len(qr_str[1]) >= 6 \
                            and len(qr_str[2]) >= 12:
                        print('store to base')
                        doc_num = db.get_last_doc_number()
                        db.create_new_scanedQR(qr_str[0], qr_str[1], qr_str[2], doc_num)
                else:
                    command_scripts.print_clone(qr_str)

            except :
                print("Unexpected error:", sys.exc_info()[0])
            # Put the rest of your code you want here

        # Optional: sleep 10 ms (0.01 sec) once per loop to let other threads on
        # your PC run during this time.
        time.sleep(0.2)

    ser.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_scan()

