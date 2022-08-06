#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from brom import *

def create_infentory_1C(list_barcode):

    # Создаем клиен
    клиент = БромКлиент("http://192.168.1.81:8080/alpana", "Administrator", "alpana")

    # Получаем информацию о конфигурации информационной базы
    #инфо = клиент.ПолучитьИнформациюОСистеме()

    # Выводим полученную информацию на экран
    #print("Конфигурация: " + инфо.Синоним)
    #print("Версия конфигурации: " + инфо.Версия)

    doc_num = клиент.brom_execute.CreateInventoryAssembly(list_barcode)

    return  doc_num

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Bc = "1002740326155";
    Bc += ";"
    Bc += "2300000060160";
    print(Bc)
    doc_num = create_infentory_1C(Bc)
    print(doc_num)
