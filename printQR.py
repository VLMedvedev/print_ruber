
import time
import socket
import argparse
import dbSqliteAlpameter as db
import os
#import sys


def print_qr_zpl_landscape(name_mat, diam, partnum, proizv, year_mon_day, formula, epoch32):

    str_print ='^XA ^POI ^PW250 ^CI0 ~SD25 ~TA000'
    str_print += '^LH5,25 ^FT120,400 ^BQR,2,3 ^FH ^FDQA,'
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

    str_print += '^FO180,45 ^FB350,1,0,J,0 ^A0R,50,32^FD'
    str_print += name_mat[0:12]
    str_print += '^FS'

    str_print += '^FO120,45 ^FB350,1,0,J,0 ^A0R,55,43^FD'
    str_print += diam
    str_print += '^FS'

    str_print += '^FO90,45 ^FB235,1,0,L,0 ^A0R,30,30^FD'
    str_print += partnum
    str_print += '^FS'

    str_print += '^FO60,280 ^FB160,1,0,L,0 ^A0R,30,28^FD'
    str_print += year_mon_day
    str_print += '^FS'

    tap = db.get_taped()
    material = tap.material
    if material == 'POLYURETHANES':
        str_print += '^FO30,300 ^FB60,1,0,L,0 ^A0R,25,24^FD'
        str_print += "#"+str(formula)
        str_print += '^FS'

    str_print += '^XZ'
    return  str_print

def print_qr_zpl(name_mat, diam, partnum, proizv, year_mon_day, formula, epoch32):

    str_print ='^XA ^PON ^PW410 ^CI0 ~SD25 ~TA000'
    str_print += '^LH5,25 ^FT270,120 ^BQN,2,3 ^FH_ ^FDQA,'
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

    str_print += '^FO15,5 ^FB250,1,0,J,0 ^A0N,50,32^FD'
    str_print += name_mat[0:12]
    str_print += '^FS'

    str_print += '^FO15,60 ^FB250,1,0,J,0 ^A0N,50,43^FD'
    str_print += diam
    str_print += '^FS'

    str_print += '^FO15,115 ^FB250,1,0,L,0 ^A0N,25,26^FD'
    str_print += partnum
    str_print += '^FS'

    str_print += '^FO270,130 ^FB160,1,0,L,0 ^A0N,25,24^FD'
    str_print += year_mon_day
    str_print += '^FS'

    str_print += '^FO300,155 ^FB160,1,0,L,0 ^A0N,22,24^FD'
    str_print += str(epoch32)[5:10]
    str_print += '^FS'

    tap = db.get_taped()
    material = tap.material
    if material == 'POLYURETHANES':
        str_print += '^FO320,180 ^FB100,1,0,L,0 ^A0N,25,24^FD'
        str_print += "#"+str(formula)
        str_print += '^FS'

    str_print += '^XZ'
    return  str_print

def print_max_qr_zpl(name_mat, diam, partnum, proizv, year_mon_day, formula, epoch32):

    str_print ='^XA ^PON ^PW410 ^CI0 ~SD25 ~TA030'
    str_print += '^LH1,1 ^FT270,195 ^BQN,2,3 ^FH_ ^FDQA,'
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

    str_print += '^FO01,01 ^XGE:max380.PNG'
    str_print += '^FS'

    name_mat = name_mat.replace('Max H-Pur ', '')
    str_print += '^FO15,75 ^FB200,1,0,R,0 ^A0N,40,40^FD'
    str_print += name_mat[0:12]
    str_print += '^FS'

    str_print += '^FO15,115 ^FB200,1,0,R,0 ^A0N,50,43^FD'
    str_print += diam
    str_print += '^FS'

    str_print += '^FO20,175 ^FB200,1,0,R,0 ^A0N,25,26^FD'
    str_print += partnum
    str_print += '^FS'

    str_print += '^FO125,165 ^FB160,1,0,R,0 ^A0N,25,24^FD'
    str_print += year_mon_day
    str_print += '^FS'

    # str_print += '^FO300,155 ^FB160,1,0,L,0 ^A0N,22,24^FD'
    # str_print += str(epoch32)[5:10]
    # str_print += '^FS'

    # formula = '13.W'
    str_print += '^FO300,195 ^FB100,1,0,L,0 ^A0N,25,24^FD'
    str_print += "#" + str(formula)
    str_print += '^FS'

    str_print += '^XZ'

    return str_print

def print_to_net_printer(str_print):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host = "192.168.1.222"
    #host = db.get_IP()
    host = '127.0.0.1'
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
       # filename = 'USB00' + str(port)
        #print(filename)
        if exists(filename):
            #print(port)
            fpw = open(filename, 'w')
            fpw.write(str_print)
            fpw.close()

def get_print_string(pr, landscape=0):
    # pr = create_new_print(p_name, p_id, p_od)
    year_mon_day = time.strftime('%Y/%m/%d')
    name = pr.name_materiar
    label = str(name)
    #max = db.get_taped_max()
    if label.find('Max') > 0:
        max = 1
    else:
        max = 0

    proizv = 'ALPANA D.O.O'
    if not (pr is None):
        # print(out_diam_array)
        diam = str(int(pr.id_nom)) + 'x' + str(int(pr.od_nom)) + 'x' + str(pr.len)
        if max == 0:
            strprint = print_qr_zpl( label, diam, pr.part_number, proizv, year_mon_day, pr.formula, pr.epoch32 )
        else:
            strprint = print_max_qr_zpl(label, diam, pr.part_number, proizv, year_mon_day, pr.formula, pr.epoch32)

        return strprint
    return None

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
    #print_to_net_printer(strLabel)
    print_direct(strLabel)

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
    parser.add_argument('--name', type=str, help='Name materials', default='Max H-Pur | FDA' )
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
    not_print = 0


    if clone == 0:
        pr = db.create_new_print(name, float(iner_diam), float(out_diam), epoch32)
        strLabel = get_print_string(pr, landscape)
        #strLabel = '^XA^FO20,20^XGR:max380p.PNG^XZ'
        #print(strLabel)
        #sys.stderr.write("strLabel = " + str(strLabel))
        if not_print == 0:
            for i in range(quantity):
                print_direct(strLabel)
                #print_to_net_printer(strLabel)
    else:
        strLabel = get_clone_print_string(name, iner_diam, out_diam, landscape, epoch32)
        #print(strLabel)
        sys.stderr.write("strLabel = " + str(strLabel))
        if not_print == 0:
            for i in range(quantity):
                print_direct(strLabel)
                #print_to_net_printer(strLabel)


#    vEvze8-dutkyw-jydnam
