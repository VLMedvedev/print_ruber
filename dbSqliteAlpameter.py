#!/usr/bin/env python3

# Импортируем нашу ORM библиотеку
from peewee import *
import string
import os
from datetime import datetime

import dbSqliteAlpameter
import  printQR
import sys
import time

import logging
logging.basicConfig(level=logging.INFO)

# Создаем соединение с нашей базой данных
conn = SqliteDatabase('alpameter.db')

# Создаем курсор - это специальный объект который делает запросы
# и получает их результаты
cursor = conn.cursor()

################ 3, ОПРЕДЕЛЯЕМ МОДЕЛИ ######################

# Определяем базовую модель о которой будут наследоваться остальные
class BaseModel(Model):

    class Meta:
        database = conn

#### Materials - begin
class Materials(BaseModel):
    id = AutoField(column_name='Index')
    type_name = TextField(column_name='TypeID')
    name = TextField(column_name='Name', null=False, unique=True)
    colour = TextField(column_name='Colour')
    minH = IntegerField(column_name='MinH')
    minS = IntegerField(column_name='MinS')
    minV = IntegerField(column_name='MinV')
    maxH = IntegerField(column_name='MaxH')
    maxS = IntegerField(column_name='MaxS')
    maxV = IntegerField(column_name='MaxV')
    minH1 = IntegerField(column_name='MinH1')
    minS1 = IntegerField(column_name='MinS1')
    minV1 = IntegerField(column_name='MinV1')
    maxH1 = IntegerField(column_name='MaxH1')
    maxS1 = IntegerField(column_name='MaxS1')
    maxV1 = IntegerField(column_name='MaxV1')
    count_min = IntegerField(column_name='CountMin')
    count_max = IntegerField(column_name='CountMax')
    count_min_1 = IntegerField(column_name='CountMin1')
    count_max_1 = IntegerField(column_name='CountMax1')
    dilate = IntegerField(column_name='Dilate')

    reverse = IntegerField(column_name='Reverse')


    class Meta:
        table_name = 'Materials'

def get_materials_for_id(p_id):
    m = Materials.get(Materials.id == p_id)
    return m

def get_materials_for_name(p_name):
    try:
        return Materials.get(Materials.name == p_name)
    except:
        return None

def get_materials_for_type_id(p_type):
    #print(p_type)
    #m = Materials.select(Materials.type_name == p_type).limit(9)
    m = Materials.select().where(Materials.type_name == p_type).limit(9)
    return m

def get_current_material_parametr():
    last_name = get_taped()
    m = get_materials_for_name(last_name.name)
    return m

def set_current_material_parametr(hMin, sMin, vMin, hMax, sMax, vMax, Mode):
    last_name = get_taped()
    m = get_materials_for_name(last_name.name)
    if Mode == 0:
        m.minH = hMin
        m.minS = sMin
        m.minV = vMin
        m.maxH = hMax
        m.maxS = sMax
        m.maxV = vMax
    else:
        m.minH1 = hMin
        m.minS1 = sMin
        m.minV1 = vMin
        m.maxH1 = hMax
        m.maxS1 = sMax
        m.maxV1 = vMax
    m.save()

    return m

def create_new_material(p_name, p_type, p_colour,
                 p_minH=0, p_minS=0, p_minV=39,
                 p_maxH=179, p_maxS=255, p_maxV=255,
                 p_minH1=0, p_minS1=0, p_minV1=59,
                 p_maxH1=255, p_maxS1=255, p_maxV1=255,
                 p_count_min=40, p_count_max=80,
                 p_count_min_1=90, p_count_max_1=130,
                 p_dilate=0, p_reverse=1):
    m = Materials(type_name=p_type, name=p_name, colour=p_colour, minH=p_minH, minS=p_minS, minV=p_minV, maxH=p_maxH, maxS=p_maxS, maxV=p_maxV, minH1=p_minH1, minS1=p_minS1, minV1=p_minV1, maxH1=p_maxH1, maxS1=p_maxS1, maxV1=p_maxV1, count_min=p_count_min, count_max=p_count_max, count_min_1=p_count_min_1, count_max_1=p_count_max_1, dilate=p_dilate, reverse=p_reverse)
    m.save()
    return m

def set_min_v_for_material(m, minv):
    m.minV = minv
    m.save()

def deleta_all_materials():
    #m = Materials.delete_instance()
    #m = Materials.delete()
    #m.execute()
    return m

#### Doors - End

##### Touch_log - begin
class Taped_log(BaseModel):
    id = AutoField(column_name='Index')
    name = TextField(column_name='Name')
    last_doc_number = IntegerField(column_name='LastDocNumber')
    epoch32 = IntegerField(column_name='Epoch32')
    material = TextField(column_name='Material')
    print = IntegerField(column_name='Print')
    formula = FloatField(column_name='Formula')
    log = TextField(column_name='Log')
    iner_diam = IntegerField(column_name='InDiam')
    out_diam = IntegerField(column_name='OutDiam')
    len = IntegerField(column_name='Len')
    max = IntegerField(column_name='Max')
    date_p = DateField(null=True)
    code_p = IntegerField(null=True)

    class Meta:
        table_name = 'Taped_log'

def set_taped_name(p_name):
    taped = Taped_log.get(Taped_log.id == 1)
    taped.name = p_name
    epoch32 = datetime.now().timestamp()
    taped.epoch32 = epoch32
    taped.save()
    # save() returns the number of rows modified.
    return taped

def set_taped_material(p_name):
    taped = Taped_log.get(Taped_log.id == 1)
    taped.material = p_name
    epoch32 = datetime.now().timestamp()
    taped.epoch32 = epoch32
    taped.save()
    # save() returns the number of rows modified.
    return taped


def set_taped_diam(iner_diam, out_diam, len):
    taped = Taped_log.get(Taped_log.id == 1)
    taped.iner_diam = (iner_diam)
    taped.out_diam = (out_diam)
    taped.len = (len)
    taped.save()
    # save() returns the number of rows modified.
    return taped

def set_taped_print(p_p):
    taped = Taped_log.get(Taped_log.id == 1)
    taped.print = p_p
    epoch32 = datetime.now().timestamp()
    taped.epoch32 = epoch32
    taped.save()
    # save() returns the number of rows modified.
    return taped

def set_taped_formula(p_p):
    taped = Taped_log.get(Taped_log.id == 1)
    taped.formula = p_p
    epoch32 = datetime.now().timestamp()
    taped.epoch32 = epoch32
    taped.save()
    # save() returns the number of rows modified.
    return taped

def set_taped_date_p(p_p):
    taped = Taped_log.get(Taped_log.id == 1)
    taped.date_p = p_p
    epoch32 = datetime.now().timestamp()
    taped.epoch32 = epoch32
    taped.save()
    # save() returns the number of rows modified.
    return taped

def set_taped_code_p(p_p):
    taped = Taped_log.get(Taped_log.id == 1)
    taped.code_p = p_p
    epoch32 = datetime.now().timestamp()
    taped.epoch32 = epoch32
    taped.save()
    # save() returns the number of rows modified.
    return taped

def set_last_doc_number(p_p):
    taped = Taped_log.get(Taped_log.id == 1)
    taped.last_doc_number = p_p
    taped.save()
    # save() returns the number of rows modified.
    return taped

def set_log(p_p):
    taped = Taped_log.get(Taped_log.id == 1)
    epoch32 = datetime.now().timestamp()
    taped.epoch32 = epoch32
    taped.log = p_p
    taped.save()
    # save() returns the number of rows modified.
    return taped

def set_taped_max(p_p):
    taped = Taped_log.get(Taped_log.id == 1)
    taped.max = p_p
    taped.save()
    # save() returns the number of rows modified.
    return taped

def get_taped_max():
    t = get_taped()
    return  t.max

def get_last_doc_number():
    t = get_taped()
    return  t.last_doc_number

def get_log():
    t = get_taped()
    return  t.log

def get_taped():
    tap = Taped_log.get(Taped_log.id == 1)
    return tap

##### Touch_log - end

##### Printed_log - begin
class Printed_log(BaseModel):
    id = AutoField(column_name='Index')
    name_materiar = TextField(column_name='NameMaterial')
    epoch32 = IntegerField(column_name='Epoch32')
    id_dia = FloatField(column_name='IDdia')
    od_dia = FloatField(column_name='ODdia')
    part_number = TextField(column_name='PartNumber')
    id_nom = FloatField(column_name='ID_nom')
    od_nom = FloatField(column_name='OD_nom')
    len = IntegerField(column_name='Len')
    formula = FloatField(column_name='Formula')
    deleted = IntegerField(column_name='Deleted')

    class Meta:
        table_name = 'Printed_log'

def create_new_print(p_name, p_id, p_od, p_epoch32, p_len=160):
    p = get_product_for_dia(p_name, p_id, p_od, p_len)
    part_number = 0
    id_nom = 0
    od_nom = 0
    if p is None:
        print("Not in price")
        return None

    part_number = p.part_number
    id_nom = (p.id_nom)
    od_nom = (p.od_nom)

    #print(part_number)

    pr = Printed_log()
    pr.part_number = part_number
    pr.id_nom = id_nom
    pr.od_nom = od_nom
    pr.len = p.len
    pr.name_materiar = p_name
    pr.id_dia = p_id
    pr.od_dia = p_od
    pr.deleted = 0
    #epoch32 = datetime.now().timestamp()
    pr.epoch32 = p_epoch32
    tap = get_taped()
    pr.formula = tap.formula
    mat = get_materials_for_name(p_name)
    pr.colour = mat.colour
    print(mat, mat.colour)
    pr.save()
    # save() returns the number of rows modified.

    doc_create_new_print( part_number, p_epoch32 )

    return pr

def get_last_printed():
    """ Печатаем последние 5 записей в таблице Doors"""
    #print('########################################################')
    cur_query = Printed_log.select()\
        .limit(1).order_by(Printed_log.id.desc())
    # .where(Printed_log.deleted != 1)\
    #for item in cur_query.dicts().execute():
    out_pr = None
    for pr in cur_query:
        out_pr = pr
    return out_pr

def delete_print_log(p_epoch32):
    cur_query = Printed_log.select().where(Printed_log.epoch32 == p_epoch32)

    out_pr = None
    for pr in cur_query:
        out_pr = pr
        out_pr.deleted = 1
        out_pr.save()
    if out_pr is None:
        return None
    #print(out_pr)
    return out_pr

def delete_print_log_all():
    cur_query = Printed_log.delete()
    cur_query.execute()

    return cur_query

##### Printed_log - end

##### ScanedQR - begin
class ScanedQR(BaseModel):
    id = AutoField(column_name='Index')
    doc_number = IntegerField(column_name='DocNumber')
    epoch32 = IntegerField(column_name='Epoch32')
    name_materiar = TextField(column_name='NameMaterial')
    part_number = TextField(column_name='PartNumber')
    diam = TextField(column_name='Diam')
    deleted = IntegerField(column_name='Deleted')

    class Meta:
        table_name = 'ScanedQR'

def delete_scanedQR(p_epoch32):
    cur_query = ScanedQR.select().where(ScanedQR.epoch32 == p_epoch32)
    out_pr = None
    for pr in cur_query:
        out_pr = pr
    if out_pr is None:
        return None

    #if out_pr.deleted != 1:
    out_pr.deleted = 1
    #else:
    #    out_pr.deleted = 0

    out_pr.save()
    #print(out_pr)
    return out_pr

def create_new_scanedQR(p_name, p_diam, p_partnum, p_doc_number):
    sc = ScanedQR()
    sc.part_number = p_partnum
    sc.name_materiar = p_name
    sc.deleted = 0
    sc.diam = p_diam
    sc.doc_number = p_doc_number
    epoch32 = datetime.now().timestamp()
    sc.epoch32 = epoch32
    sc.save()
    # save() returns the number of rows modified.

    doc_mark_print_scaned(p_partnum, epoch32)

    return sc

def get_last_scanedQR():
    """ Печатаем последние 5 записей в таблице Doors"""
    #print('########################################################')
    cur_query = ScanedQR.select() \
        .where(ScanedQR.deleted != 1)\
        .limit(1).order_by(ScanedQR.id.desc())

    #.where(ScanedQR.doc_number == p_doc_number) \

    out_pr = None
    for pr in cur_query:
        out_pr = pr
    if out_pr is None:
        return None
    return out_pr

def get_last_scanedQR_for_1c(p_doc_number):
    """ Печатаем последние 5 записей в таблице Doors"""
    #print('########################################################')
    cur_query = ScanedQR.select() \
        .where((ScanedQR.doc_number == p_doc_number) & (ScanedQR.deleted != 1)) \
        .order_by(ScanedQR.part_number)

    return cur_query

##### ScanedQR - end

##### Doc - begin
class Doc(BaseModel):
    id = AutoField(column_name='Index')
    #doc_number = IntegerField(column_name='DocNumber')
    part_number = TextField(column_name='PartNumber')
    name_materiar = TextField(column_name='NameMaterial')
    diam = TextField(column_name='Diam')
    print_epoch32 = IntegerField(column_name='PrintEpoch32')
    scan_epoch32 = IntegerField(column_name='ScanEpoch32')
    delp = IntegerField(column_name='DelP')
    dels = IntegerField(column_name='DelS')

    class Meta:
        table_name = 'Doc'

def doc_delete_Print(p_epoch32):
    cur_query = Doc.select().where(Doc.print_epoch32 == p_epoch32)
    out_pr = None
    for pr in cur_query:
        out_pr = pr
    if out_pr is None:
        return None

    out_pr.delp = 1
    out_pr.save()
    #print(out_pr)
    return out_pr

def doc_delete_scanedQR(p_epoch32):
    cur_query = Doc.select().where(Doc.scan_epoch32 == p_epoch32)
    out_pr = None
    for pr in cur_query:
        out_pr = pr
    if out_pr is None:
        return None

    if out_pr.print_epoch32 != 0:
        out_pr.scan_epoch32 = 0
        #out_pr.dels = 1
    else:
        #if out_pr.dels != 1:
        out_pr.dels = 1
        #else:
       #     out_pr.dels = 0
    out_pr.save()
    #print(out_pr)
    return out_pr

def doc_create_new_print( p_partnum, p_epoch32):
    pr = get_product_for_part_number(p_partnum)
    p_name = pr.name_material
    p_diam = str(int(pr.id_nom))
    p_diam += '*'
    p_diam += str(int(pr.od_nom))
    p_diam += '*'
    p_diam += str(pr.len)

    sc = Doc()
    sc.part_number = p_partnum
    sc.name_materiar = p_name
    sc.delp = 0
    sc.dels = 0
    sc.diam = p_diam
    #sc.doc_number = p_doc_number
    #epoch32 = datetime.now().timestamp()
    sc.print_epoch32 = p_epoch32
    sc.scan_epoch32 = 0
    sc.save()
    # save() returns the number of rows modified.
    return sc

def doc_create_new_scanedQR(p_partnum, p_epoch32):
    pr = get_product_for_part_number(p_partnum)
    p_name  = pr.name_material
    p_diam = str(pr.id_nom)
    p_diam += '*'
    p_diam += str(pr.od_nom)
    p_diam += '*'
    p_diam += str(pr.len)

    sc = Doc()
    sc.part_number = p_partnum
    sc.name_materiar = p_name
    sc.dels = 0
    sc.delp = 0
    sc.diam = p_diam
    #sc.doc_number = p_doc_number
    sc.scan_epoch32 = p_epoch32
    sc.print_epoch32 = 0
    sc.save()
    # save() returns the number of rows modified.
    return sc

def doc_mark_print_scaned(p_partnum, p_epoch32):
    cur_query = Doc.select()\
        .where((Doc.dels != 1) \
            & (Doc.part_number == p_partnum) \
            & (Doc.scan_epoch32 == 0 )) \
        .limit(1).order_by(Doc.print_epoch32.desc())

    f_not_print = True
    for pr in cur_query:
        pr.scan_epoch32 = p_epoch32
        pr.dels = 0
        pr.save()
        f_not_print = False

    if f_not_print:
        #print("Not printed")
        doc_create_new_scanedQR( p_partnum, p_epoch32)

def doc_clear_all():
    Doc.delete().execute()

def doc_get_last():
    """ Печатаем последние 5 записей в таблице Doors"""
    #print('########################################################')
    cur_query = Doc.select().where((Doc.delp != 1) & (Doc.dels != 1)).limit(12).order_by(Doc.id.desc())
    return cur_query

def doc_for_1c():
    """ Печатаем последние 5 записей в таблице Doors"""
    #print('########################################################')
    cur_query = Doc.select().where((Doc.scan_epoch32 != 0) & (Doc.delp != 1) & (Doc.dels != 1)).order_by(Doc.part_number)

    return cur_query

##### Doc - end

##### Products - begin
class Products(BaseModel):
    id = AutoField(column_name='Index')
    part_number = TextField(column_name='PartNumber')
    name_material = TextField(column_name='Material')
    id_nom = FloatField(column_name='ID_nom')
    od_nom = FloatField(column_name='OD_nom')
    len = IntegerField(column_name='Len')
    weight = FloatField(column_name='Weight')
    id_pic = IntegerField(column_name='ID_pic')
    od_pic = IntegerField(column_name='OD_pic')

    class Meta:
        table_name = 'Products'

def create_new_product(p_part_number, p_name, p_id, p_od, p_len, p_weight):
    pr = Products()
    pr.part_number = p_part_number
    pr.name_material = p_name
    pr.id_nom = p_id
    pr.od_nom = p_od
    pr.len = p_len
    pr.weight = p_weight
    pr.save()
    # save() returns the number of rows modified.
    return pr

def get_product_for_dia(p_name, p_in, p_od, p_len=160):
    str_log = f"get produkt  ID {p_in} OD {p_od} Len {p_len} "
    logging.info(str_log)
    tolerance = 0.4
    delta_diam = p_od - p_in
    koeff_tolsh = delta_diam / 20
    proc_in = p_in / 100
    proc_out = p_od / 100
    tlr_in = tolerance
    tlr_out = tolerance

    #m = Materials.select(Materials.type_name == p_type).limit(9)
    #cur_query = Products.select().where((Products.name_material == p_name) & \
              #( Products.id_nom.between(p_in - tlr, p_in + tlr )) & \
              #( Products.od_nom.between(p_od - tlr , p_od + tlr)))

    pr_min_dia = None
    p_name = p_name.strip()

    ids = p_in - tlr_in
    cur_query = Products.select().where( \
        (Products.name_material == p_name) & \
        (Products.id_nom >= ids)). \
        order_by(Products.id).limit(2)

   # (Products.id_nom >= (p_in + tlr_in))). \

    test_diam_array = []

    for pr in cur_query:
        print(pr.part_number)
        pr_min_dia = pr
        min_dia = pr_min_dia.id_nom
        ods = p_od + tlr_out
        cur_query = Products.select().where(\
            (Products.name_material == p_name) & \
            (Products.len == p_len) & \
            (Products.id_nom == min_dia) & \
            (Products.od_nom <= ods)).\
            order_by(Products.id.desc()).limit(1)

        out_pr = None
        for pr in cur_query:
            print(pr.part_number)
            out_pr = pr
            test_diam_array.append(out_pr)

    print(test_diam_array)
 #   (Products.od_nom <= (p_od - tlr_out))). \


    if pr_min_dia is None:
        print("Not found min dia")
        return None

    if out_pr is None:
        #print("Not found max dia")
        return None
    PI = 3.14
    out_s = PI * p_od * p_od  / 4
    in_s = PI * p_in * p_in / 4
    plosha_fakt =  out_s - in_s
    min_s = 999999999
    min_pr = None

    for pr in test_diam_array:
        in_d = pr.id_nom
        od_d = pr.od_nom
        out_s_p = PI * od_d * od_d / 4
        in_s_p = PI * in_d * in_d / 4
        plosha_p = out_s_p - in_s_p
        delta_s_p = plosha_fakt - plosha_p
        if min_s > delta_s_p:
            min_s = delta_s_p
            min_pr = pr

    if min_pr is None:
        print("Not found max dia")
        return None

    return min_pr

def get_product_for_part_number(p_part_number):
    cur_query = Products.select().where(Products.part_number == p_part_number)
    out_pr = None
    for pr in cur_query:
        #print(pr.part_number)
        out_pr = pr
    return out_pr

def set_pic_for_produckt(p_produckt, p_in, p_out):
    if p_produckt  is None:
        return False
    p_produckt.id_pic = p_in
    p_produckt.od_pic = p_out
    p_produckt.save()
    return True

def deleta_all_produts():
    #m = Materials.delete_instance()
    m = Products.delete()
    m.execute()
    return m

##### Product - end

##### Settings - begin
class Settings(BaseModel):
    id = AutoField(column_name='Index')
    IP = TextField(column_name='IP')
    started = IntegerField(column_name='Started')
    zoom = IntegerField(column_name='Zoom')
    calibrate = IntegerField(column_name='Calibrate')
    testzone = IntegerField(column_name='TestZone')
    center_x = FloatField(column_name='CenterX')
    center_y = FloatField(column_name='CenterY')
    refrash = IntegerField(column_name='Refrash')
    startLoadVideo = IntegerField(column_name='StartLoadVideo')
    camera_pole_zoom_0 = IntegerField(column_name='CameraPoleZoom_0')
    camera_pole_zoom_1 = IntegerField(column_name='CameraPoleZoom_1')
    not_print = IntegerField(column_name='NotPrint')
    clone = IntegerField(column_name='Clone')

    class Meta:
        table_name = 'Settings'

def get_camera_pole_zoom_0():
    m = Settings.get(Settings.id == 1)
    return m.camera_pole_zoom_0

def get_camera_pole_zoom_1():
    m = Settings.get(Settings.id == 1)
    return m.camera_pole_zoom_1

def get_IP():
    m = Settings.get(Settings.id == 1)
    return m.IP

def get_started():
    m = Settings.get(Settings.id == 1)
    return m.started

def get_calibrate():
    m = Settings.get(Settings.id == 1)
    return m.calibrate

def get_testzone():
    m = Settings.get(Settings.id == 1)
    return m.testzone

def get_zoom():
    m = Settings.get(Settings.id == 1)
    return m.zoom /100

def get_center_x_y():
    m = Settings.get(Settings.id == 1)
    return m.center_x , m.center_y

def get_refrash():
    m = Settings.get(Settings.id == 1)
    return m.refrash

def get_startedLoadVideo():
    m = Settings.get(Settings.id == 1)
    return m.startLoadVideo

def get_not_print():
    m = Settings.get(Settings.id == 1)
    return m.not_print

def get_clone():
    m = Settings.get(Settings.id == 1)
    return m.clone

def set_clone(p_clone ):
    m = Settings.get(Settings.id == 1)
    m.clone = p_clone
    m.save()
    sys.stderr.write("Set clone: " + str(p_clone))
    return m

def set_not_print(p_not_print ):
    m = Settings.get(Settings.id == 1)
    m.not_print = p_not_print
    m.save()
    sys.stderr.write("Set not_print: " + str(p_not_print))
    return m


def set_startedLoadVideo(p_started ):
    m = Settings.get(Settings.id == 1)
    m.startLoadVideo = p_started
    m.save()
    return m

def set_refrash(p_refrash ):
    m = Settings.get(Settings.id == 1)
    m.refrash = p_refrash
    m.save()
    return m

def set_center_x_y(c_x, c_y ):
    m = Settings.get(Settings.id == 1)
    m.center_x = c_x
    m.center_y = c_y
    m.save()
    return m

def set_started(p_started):
    m = Settings.get(Settings.id == 1)
    m.started = p_started
    m.save()
    return m

def set_calibrate(p_calibr):
    m = Settings.get(Settings.id == 1)
    m.calibrate = p_calibr
    m.save()
    return m

def set_testzone(p_tz):
    m = Settings.get(Settings.id == 1)
    m.testzone = p_tz
    m.save()
    return m

def set_zoom(p_zoom):
    m = Settings.get(Settings.id == 1)
    m.zoom = p_zoom * 100
    m.save()
    return m

##### Touch_log - end

##### Koefficients - begin
class Koefficients(BaseModel):
    id = AutoField(column_name='Index')
    zoom = IntegerField(column_name='Zoom')
    picsels = IntegerField(column_name='Picsels')
    inerouter = IntegerField(column_name='InerOuter')
    koef = FloatField(column_name='Koef')
    correction = IntegerField(column_name='Correction')
    dilate = IntegerField(column_name='Dilate')

    class Meta:
        table_name = 'Koefficients'

def get_koefficient(p_zoom, p_iner, p_picsel, p_dilate ):
    #cur_query = Koefficients.select(Koefficients.zoom.distinct()).where(
    k_out = None
    zoom = int(p_zoom * 100)
    cur_query = Koefficients.select().where( \
        (Koefficients.inerouter >= p_iner) & \
     #   (Koefficients.zoom == zoom) & \
     #   (Koefficients.dilate == p_dilate) & \
        (Koefficients.picsels == p_picsel) \
        ).order_by(Koefficients.inerouter).limit(1)

    for k in cur_query:
        ##print(k)
        k_out = k

    if k_out is None:
        #print("Not found min dia")
        return None

    return k_out

##### Koefficients - end

def unregister(self):
    # classregistry.unregister(self)
    # Не забываем закрыть соединение с базой данных в конце работы
    conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #pr = get_product_for_dia('H-Pur | FDA', 14, 55 )
    #create_new_scanedQR(name,diam,partnum)
    epoch32 = '1632136279'
    epoch32 = datetime.now().timestamp()

    name = "H-NBR"
    iner_diam = 0
    out_diam = 20
    len=600
    epoch32 = 1633420201.52626

    p = get_product_for_dia(name, iner_diam, out_diam, len)
    print(p.id)
    print(p.part_number)
    #pr = create_new_print(name, iner_diam, out_diam, epoch32, len)

    #delete_print_log_all()

    #delete_print_log(epoch32)
    #delete_scanedQR(epoch32)
    #doc_mark_print_scaned(partnum, epoch32)




