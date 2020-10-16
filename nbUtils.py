#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ${NAME}.py
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
${DATE} ${TIME}   gxrao      1.0         None
'''

import json

import serial as se


def readConf(confPath='config.json'):
    """

    :param confPath:
    :return:
    """
    data = []
    with open(confPath, 'r') as f:
        data = json.load(f)
    return data


def writeConfg(configPath="config.json"):
    data = []
    with open(configPath, 'w') as f:
        json.dump(data, f)


def getSe(devPath='/dev/input/ttyUSB0', isDefault=True, **kwargs):
    if (isDefault ==True):
        thisSerial = se.Serial(port=devPath, baudrate=9600, bytesize=se.EIGHTBITS, parity=se.PARITY_NONE)

    return thisSerial
