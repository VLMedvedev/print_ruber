#!/usr/bin/env   python3

from openpyxl import load_workbook
import dbSqliteAlpameter as db


def import_price_xls():
    #db.deleta_all_produts()
    #return

    print('Main Begin')
    wb = load_workbook('Products1.xlsx')

    for sheet_name in wb.sheetnames:
        print(sheet_name)
        if sheet_name is None:
            continue
        if sheet_name == 'SUMMARY' \
            or sheet_name == 'Wear Tapes' \
            or sheet_name == 'Modifications' \
            or sheet_name == 'Tools | Holders' \
            or sheet_name == 'Springs' :
            continue
        sheet = wb[sheet_name]
        # to print the maximum number of occupied rows in console
        #print(sheet.max_row)
        # считываем значение определенной ячейки
        #val = sheet['A3'].value
        #print(val)
        # iterate over all rows
        for i in range(3, sheet.max_row - 4):
            new = str(sheet.cell(row=i, column=10).value)
            #print(new)
           # if new.find('New') == -1:
            #    continue
            part_number = sheet.cell(row=i, column=20).value
            if str(part_number).find('=') >= 0:
                part_number = sheet.cell(row=i, column=1).value
            #print(part_number)
            if part_number is None:
                continue
            name_material = str(sheet.cell(row=i, column=3).value)
            if name_material.startswith("TFE"):
                name_material = 'TFEP | FEPM'
            #print(name_material)
            id_nom = sheet.cell(row=i, column=5).value

            od_nom = sheet.cell(row=i, column=7).value
            #print(od_nom)
            len = sheet.cell(row=i, column=9).value
            #print(len)
            weight = sheet.cell(row=i, column=12).value
            #print(weight)

            db.create_new_product(part_number, \
                                  name_material, \
                                  id_nom, od_nom, \
                                  len, weight )

def import_price_csv():
    print('Main Begin')
    fileread = open('product.csv', 'r')
    countstr = 0

    for line in fileread:
        str_array = line.split(';')
        countstr += 1
        part_number = str_array[0]
        print(part_number)
        name_material = str_array[2]
        print(name_material)
        id_nom = str_array[4]
        print(id_nom)
        od_nom = str_array[6]
        print(od_nom)
        len = str_array[8]
        print(len)
        weight = str_array[11]
        print(weight)

        db.create_new_product(part_number, \
                                  name_material, \
                                  id_nom, od_nom, \
                                  len, weight )

    fileread.close()

if __name__ == '__main__':
    #import_price_csv()
    import_price_xls()


    '''
H-Pur | FDA
SH-Pur
H-Pur TQ
H-Pur Green
H-Pur Blue | FDA
H-Pur Nat. | FDA
LT-Pur
XH-Pur
XSH-Pur
NBR
FKM | FDA
FKM Black
EPDM | FDA
H-NBR
MVQ | FDA
MVQ Blue | FDA
MVQ Nat | FDA
TFEP | FEPM | Aflas
POM | FDA
PA6 | FDA
PTFE-1 | FDA
PTFE-2
PTFE-3
PTFE-4
    '''