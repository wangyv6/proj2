#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from mUtils import getSerial ,writeMsg,serialSendMsg    

def getBalence():
    ser = getSerial()   
    ret = serialSendMsg()   
    return ret