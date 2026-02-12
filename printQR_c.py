#!/usr/bin/env python3
#import qrcode
#import os
#import numpy
#import cv2
#from PIL import Image
import time
import socket
import argparse
import dbSqliteAlpameter as db
import os
#import sys

def print_qr_zpl_landscape(name_mat, diam, partnum, proizv, year_mon_day, formula, epoch32):

    str_print ='^XA ^POI ^PW580 ^CI0 ~SD24 ~TA020'
    str_print += '^LH5,5 ^FT200,595 ^BQR,2,5 ^FH_ ^FDQA,'
    str_print += name_mat
    str_print += '_0D_0A'

    str_print += diam
    str_print += '_0D_0A'

    str_print += partnum
    str_print += '_0D_0A'

    str_print += proizv
    str_print += '_0D_0A'

    #str_print += year_mon_day
    #str_print += '_0D_0A'
    #str_print += str(formula)
    #str_print += '_0D_0A'
    #str_print += str(epoch32)
    #str_print += '_0D_0A'
    str_print +=  '^FS'

    str_print += '^FO380,15 ^FB575,1,0,J,0 ^A0R,85,65^FD'
    str_print += name_mat[:15]
    str_print += '^FS'

    str_print += '^FO280,5 ^FB340,1,0,C,0 ^A0R,80,65^FD'
    str_print += diam
    str_print += '^FS'

    str_print += '^FO240,5 ^FB340,1,0,C,0 ^A0R,35,35^FD'
    str_print += partnum
    str_print += '^FS'

    tap = db.get_taped()
    material = tap.material
    code_p = str(tap.code_p)
    date_p = tap.date_p
    formula = tap.formula
#    year_mon_day = date_p.strftime('%Y/%m/%d')
    year_mon_day = date_p.strftime('%d/%m/%Y')

    str_print += '^FO190,160 ^FB260,1,0,L,0 ^A0R,35,38^FD'
    str_print += year_mon_day
    str_print += '^FS'

    if material == 'POLYURETHANES':
        str_print += '^FO140,400 ^FB160,1,0,L,0 ^A0R,35,35^FD'
        str_print += "#"+str(formula)
        str_print += '^FS'

    str_print += '^XZ'
    return  str_print

def print_max_qr_zpl_landscape(name_mat, diam, partnum, proizv, year_mon_day, formula, epoch32, colour):

    str_print ='^XA ^POI ^PW580 ^CI0 ~SD24 ~TA020'
    str_print += max_string_landscape(name_mat)
    str_print += '^LH5,5 ^FT200,595 ^BQR,2,5 ^FH_ ^FDQA,'
    str_print += name_mat
    str_print += '_0D_0A'

    str_print += diam
    str_print += '_0D_0A'

    str_print += partnum
    str_print += '_0D_0A'

    str_print += proizv
    str_print += '_0D_0A'

    #str_print += year_mon_day
    #str_print += '_0D_0A'
    #str_print += str(formula)
    #str_print += '_0D_0A'
    #str_print += str(epoch32)
    #str_print += '_0D_0A'
    str_print +=  '^FS'

    #str_print += '^FO260,15 ^FB355,1,0,J,0 ^A0R,85,65^FD'
    #str_print += name_mat
    #str_print += '^FS'

    str_print += '^FO280,30 ^FB340,1,0,L,0 ^A0R,80,55^FD'
    str_print += diam
    str_print += '^FS'

    str_print += '^FO240,160 ^FB390,1,0,L,0 ^A0R,35,35^FD'
    str_print += colour
    str_print += '^FS'
#    str_print += '^F220,25 ^FB355,1,0,L,0 ^A0R,35,40^FD'
#    str_print += colour
#    str_print += '^FS'

    tap = db.get_taped()
    material = tap.material
    code_p = str(tap.code_p)
    date_p = tap.date_p
    formula = tap.formula
    year_mon_day = date_p.strftime('%d/%m/%Y')

    str_print += '^FO190,160 ^FB260,1,0,L,0 ^A0R,35,38^FD'
    str_print += year_mon_day
    str_print += '^FS'


    #if material == 'POLYURETHANES':
    str_print += '^FO140,400 ^FB160,1,0,L,0 ^A0R,35,35^FD'
    str_print += "#"+str(formula)
    str_print += '^FS'

    str_print += '^XZ'
    return  str_print

def max_string_landscape(name_mat=''):
    #name_mat = name_mat.replace('Max ', '')
    name_mat=name_mat.upper()
    hpur_position = name_mat.find("H-PUR")
    name_mat = name_mat[4:hpur_position+5]
    str_print = '^LRY'
    str_print += '^FO385,30'
    str_print += '^GB90,180,90,,2^FS'
    str_print += '^FO380,45'
    str_print += '^A@R,80,65,E:A.TTF'
    str_print += '^FDMax^FS'
    str_print += '^FO380,240'
    str_print += '^A@R,80,65,E:A.TTF'
    #namex='XSH-PUR'
    str_print += f'^FD{name_mat}^FS'
    return str_print


def print_qr_zpl(name_mat, diam, partnum, proizv, year_mon_day, formula, epoch32):

    str_print ='^XA ^PON ^PW580 ^CI0 ~SD30  ~TA040'
    str_print += '^LH25,5 ^FT370,240 ^BQN,2,4 ^FH_ ^FDQA,'
    str_print += name_mat
    str_print += '_0D_0A'
    str_print += diam
    str_print += '_0D_0A'
    str_print += partnum
    str_print += '_0D_0A'
    str_print += proizv
    str_print += '_0D_0A'
    #str_print += year_mon_day
    #str_print += '_0D_0A'
    #str_print += str(formula)
    #str_print += '_0D_0A'
    #str_print += str(epoch32)
    #str_print += '_0D_0A'
    str_print +=  '^FS'

    str_print += '^FO15,50 ^FB350,1,0,J,0 ^A0N,70,48^FD'
    str_print += name_mat[:15]
    str_print += '^FS'

    str_print += '^FO15,130 ^FB350,1,0,J,0 ^A0N,80,60^FD'
    str_print += diam
    str_print += '^FS'

    #str_print += '^FO15,215 ^FB350,1,0,L,0 ^A0N,35,40^FD'
    #str_print += partnum
    #str_print += '^FS'

    tap = db.get_taped()
    material = tap.material
    code_p = ""
    #date_p = tap.date_p
    formula = ""
    year_mon_day = ""
    #year_mon_day = date_p.strftime('%Y/%m/%d')



    str_print += '^FO370,215 ^FB260,1,0,L,0 ^A0N,35,35^FD'
    str_print += year_mon_day
    str_print += ' #'
    str_print += code_p
    str_print += '^FS'

    #str_print += '^FO400,270 ^FB260,1,0,L,0 ^A0N,28,30^FD'
    #str_print += epoch32[2:10]
    #str_print += '^FS'


    if material == 'POLYURETHANES':
        str_print += '^FO380,280 ^FB150,1,0,L,0 ^A0N,35,34^FD'
        str_print += "#"+str(formula)
        str_print += '^FS'

    str_print += '^XZ'
    return  str_print

def max_string(name_mat=''):
    #name_mat = name_mat.replace('Max ', '')
    name_mat=name_mat.upper()
    hpur_position = name_mat.find("H-PUR")
    name_mat = name_mat[4:hpur_position+5]
    str_print = '^LRY'
    str_print += '^FO10,30'
    str_print += '^GB195,90,90,,2^FS'
    str_print += '^FO30,45'
    str_print += '^A@N,80,65,E:A.TTF'
    str_print += '^FDMax^FS'
    str_print += '^FO220,45'
    str_print += '^A@N,80,65,E:A.TTF'
    #namex='XSH-PUR'
    str_print += f'^FD{name_mat}^FS'
    return str_print

def print_max_qr_zpl(name_mat, diam, partnum, proizv, year_mon_day, formula, epoch32, colour):

    str_print ='^XA ^PON ^PW580 ^CI0  ~SD30 ~TA040'
    str_print += max_string(name_mat)
    str_print += '^LH25,5 ^FT370,310 ^BQN,2,4 ^FH_ ^FDQA,'
    str_print += name_mat
    str_print += '_0D_0A'
    str_print += diam
    str_print += '_0D_0A'
    str_print += partnum
    str_print += '_0D_0A'
    str_print += proizv
    str_print += '_0D_0A'
    #str_print += year_mon_day
    #str_print += '_0D_0A'
    #str_print += str(formula)
    #str_print += '_0D_0A'
    #str_print += str(epoch32)
    #str_print += '_0D_0A'

    str_print +=  '^FS'

    #str_print += '^FO15,30 ^FB350,1,0,J,0 ^A0N,70,48^FD'
    #str_print += name_mat[:15]
    #str_print += '^FS'
    #str_print += '^FO01,30^XGE:max560.PNG'
    #str_print += '^FS'

   # name_mat = name_mat.replace('Max H-Pur ', '')
   # str_print += '^FO15,130 ^FB300,1,0,R,0 ^A0N,50,50^FD'
   # str_print += name_mat[0:12]
   # str_print += '^FS'


    str_print += '^FO10,135 ^FB340,1,0,C,0 ^A0N,65,65^FD'
    str_print += diam
    str_print += '^FS'

    str_print += '^FO15,205 ^FB300,1,0,C,0 ^A0N,35,40^FD'
    str_print += colour
    str_print += '^FS'

    tap = db.get_taped()
    material = tap.material
    code_p = str(tap.code_p)
    date_p = tap.date_p
    formula = tap.formula
#    year_mon_day = date_p.strftime('%Y/%m/%d')
    year_mon_day = date_p.strftime('%d/%m/%Y')

    str_print += '^FO15,245 ^FB300,1,0,R,0 ^A0N,35,35^FD'
    str_print += year_mon_day
    str_print += ' #'
    str_print += code_p
    str_print += '^FS'

    str_print += '^FO380,290 ^FB150,1,0,L,0 ^A0N,35,34^FD'
    str_print += "#"+str(formula)
    str_print += '^FS'

    str_print += '^XZ'
    return  str_print


def max_string_wide(name_mat=''):
    #name_mat = name_mat.replace('Max ', '')
    name_mat=name_mat.upper()
    itOutlet=False
    if name_mat.find('OUT') >= 0:
        itOutlet=True
    hpur_position = name_mat.find("H-PUR")
    name_mat = name_mat[4:hpur_position+5]
    if itOutlet:
        name_mat += " OUT"
        str_print = '^LRY'
        str_print += '^FO15,100'
        str_print += '^GB125,60,60,,2^FS'
        str_print += '^FO025,115'
        str_print += '^A@N,35,30,E:A.TTF'
        str_print += '^FDMax^FS'
        str_print += '^FO150,115'
        str_print += '^A@N,35,25,E:A.TTF'
    else:
        str_print = '^LRY'
        str_print += '^FO105,100'
        str_print += '^GB125,60,60,,2^FS'
        str_print += '^FO120,115'
        str_print += '^A@N,45,35,E:A.TTF'
        str_print += '^FDMax^FS'
        str_print += '^FO240,115'
        str_print += '^A@N,45,35,E:A.TTF'
    #namex='XSH-PUR'
    str_print += f'^FD{name_mat}^FS'
    return str_print
def print_max_wide_qr_zpl(name_mat, diam, partnum, proizv, year_mon_day, formula, epoch32, colour):

    str_print ='^XA ^PON ^PW700 ^CI0  ~SD30 ~TA040'
    str_print += max_string_wide(name_mat)
    str_print += '^LH25,15 ^FT440,270 ^BQN,2,5 ^FH_ ^FDQA,'

    str_print += name_mat
    str_print += '_0D_0A'
    str_print += diam
    str_print += '_0D_0A'
    str_print += partnum
    str_print += '_0D_0A'
    str_print += proizv
    str_print += '_0D_0A'

    str_print +=  '^FS'

    str_print += '^FO45,25 ^FB420,1,0,C,0 ^A0N,65,65^FD'
    str_print += diam
    str_print += '^FS'

    str_print += '^FO205,175 ^FB200,1,0,C,0 ^A0N,35,40^FD'
    str_print += colour
    str_print += '^FS'

    tap = db.get_taped()
    material = tap.material
    code_p = "11"
    date_p = ""
    formula = "eee"
#    year_mon_day = date_p.strftime('%Y/%m/%d')
    year_mon_day = "01.01.01"

    str_print += '^FO135,225 ^FB300,1,0,R,0 ^A0N,30,30^FD'
    str_print += year_mon_day
    str_print += ' #'
    str_print += code_p
    str_print += '^FS'

    str_print += '^FO100,175 ^FB150,1,0,L,0 ^A0N,35,34^FD'
    str_print += "#"+str(formula)
    str_print += '^FS'

    str_print +=  '^FO0,015^GFA,536,536,8,,7OFE3C71E:::78M01E3C71E:::::::::::::78M01E3871E78M01EI01E:::78M01EI03C:78M01EI07C78M01EI0F878M03E003F,3CM03C03FE,3CM03C03FC,3EM07C03F8,1EM07803E,1FM0F8038,0F8K01F0038,07CK03E0038,07EK07C0038,03F8I01F80038,00FFI0FFI038,007FF9FFEI038,003FF9FF8I038,I07F9FEJ038,J0F9FK038,J079EK038,::::::::J070EK038,J0F0FK038,::I01E078J038,I03E07CJ038,I03C03CJ038,I0FC03EJ038,001F801F8I038,007FI0FEI038,3FFEI07FFC038,3FF8I01FFC038,3FFK0FFC038,3F8K01FC038,,^FS'

    str_print += '^XZ'
    return  str_print


def print_to_net_printer(str_print):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.0.221"
    #host = db.get_IP()
    #host = '127.0.0.1'
    port = 9100

    try:
        mysocket.connect((host, port))  # connecting to host
        mysocket.send(bytes(str_print, "utf-8"))
        mysocket.close()  # closing connection
    except:
        print("Error with the connection")

def exists(path):
    """Test whether a path exists.  Returns False for broken symbolic links"""
    try:
        os.stat(path)
    except OSError:
        return False
    return True

def print_direct(str_print):
    for port in range(2):
        filename = '/dev/usb/lp'+str(port)
        #print(filename)
        if exists(filename):
            #print(port)
            fpw = open(filename, 'w')
            fpw.write(str_print)
            fpw.close()

def get_print_string(pr, landscape=0):
    if pr is None:
        return None    
    # print(out_diam_array)


    # pr = create_new_print(p_name, p_id, p_od)
    year_mon_day = time.strftime('%Y/%m/%d')
#    year_mon_day = '2023/03/22'
    name = pr.name_materiar
    label = str(name)
    #max = db.get_taped_max()
    if label.find('Max') >= 0:
        max = 1
    else:
        max = 0

    strprint = None

    proizv = 'ALPANA D.O.O'
    if landscape == 1:
        diam = str(int(pr.id_nom)) + 'x' + str(int(pr.od_nom)) + 'x' + str(pr.len)
        if max == 0:
            strprint = print_qr_zpl_landscape( label, diam, pr.part_number, proizv, year_mon_day, pr.formula, pr.epoch32 )
        else:
            strprint = print_max_qr_zpl_landscape(label, diam, pr.part_number, proizv, year_mon_day, pr.formula, pr.epoch32, str(pr.colour))
    else:
        # print(out_diam_array)
        diam = str(int(pr.id_nom)) + 'x' + str(int(pr.od_nom)) + 'x' + str(pr.len)
        if max == 0:
            strprint = print_qr_zpl( label, diam, pr.part_number, proizv, year_mon_day, pr.formula, pr.epoch32 )
        else:
            strprint = print_max_wide_qr_zpl(label, diam, pr.part_number, proizv, year_mon_day, pr.formula, pr.epoch32, str(pr.colour))
#            strprint = print_max_qr_zpl(label, diam, pr.part_number, proizv, year_mon_day, pr.formula, pr.epoch32, str(pr.colour))

    return strprint

def get_clone_print_string(name, diam, partnum, landscape, epoch32):
    # pr = create_new_print(p_name, p_id, p_od)
    year_mon_day = time.strftime('%Y/%m/%d')
    proizv = 'ALPANA D.O.O'
   # epoch32 = str(datetime.now().timestamp())
    #if landscape == 0:
    strprint = print_qr_zpl(name, str(diam), str(partnum), proizv, year_mon_day,"",epoch32)
    #else:
    #    strprint = print_qr_zpl_landscape(name, str(diam), str(partnum), proizv, year_mon_day,"",epoch32)

    return strprint

def reprint():
    pr = db.get_last_printed()
    strLabel = get_print_string(pr)
    #print(strLabel)
    print_to_net_printer(strLabel)
    #print_direct(strLabel)

    # Press the green button in the gutter to run the script.

def load_image_to_printer(p_image_name):
    fr = open(p_image_name,'r')
    str_image = '^XA '
    str_image += fr.read()
    str_image += ' ^XZ'
    fr.close()
    return str_image

def test_image_print():
    #load_str = load_image_to_printer('max380.zpl')
    #print_direct(load_str + '\n')
    str_print = '^XA ^FO02,02 ^XGE:max380.PNG ^XZ'
    #str_print = '^XA ^FO20,20 ^FDWAR INC.^FS  ^XZ'
    print_direct(str_print + '\n')

if __name__ == '__main__':
    #test_image_print()
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, help='Name materials', default='H-Pur | FDA' )
    parser.add_argument('--iner', help='Iner diametre', default=122)
    parser.add_argument('--outer', help='OOuter diam', default=168)

    parser.add_argument('--epoch32', type=str, help='epoch32', default=1234567890)
    parser.add_argument('--quantity', type=int, help='quantity labels', default=1)
    parser.add_argument('--landscape', type=int, help='landscape=1 portrain=0', default=0)
    parser.add_argument('--clone', type=int, help='clone=1 new=0', default=0)
    args = parser.parse_args()
    name = args.name
    iner_diam = args.iner
    out_diam = args.outer
    epoch32 = str(args.epoch32)
    quantity = args.quantity
    landscape = 0 #args.landscape
    
    clone = args.clone

    not_print = db.get_not_print()
    #not_print = 0
    if clone == 0:
        pr = db.create_new_print(name, float(iner_diam), float(out_diam), epoch32)
        strLabel = get_print_string(pr, landscape)
        #strLabel = '^XA^FO20,20^XGR:max380p.PNG^XZ'
        print(f"strLabel  {strLabel}")
        #sys.stderr.write("strLabel = " + str(strLabel))
        if not_print == 0:
            for i in range(quantity):
                #print_direct(strLabel)
                print_to_net_printer(strLabel)
    else:
        strLabel = get_clone_print_string(name, iner_diam, out_diam, landscape, epoch32)
        #print(strLabel)
        #sys.stderr.write("strLabel = " + str(strLabel))
        if not_print == 0:
            for i in range(quantity):
                #print_direct(strLabel)
                print_to_net_printer(strLabel)


