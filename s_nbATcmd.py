#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from mUtils import serialSendMsg  ,readConf ,getSerial
import time


ser = getSerial()
# AT_CMD = ["AT+CGREG?","AT+MIPLCREATE"]


def signalCallBack():
    print("signal too week")

# 获取信号强度
def getSignal():  
    r""" 获得信号强度 """
    ret = serialSendMsg('AT+CSQ',ser=ser)
    
    return int(ret[1])


# 开机时初始化链接
def initConnect():
    signal=   getSignal()   
    while(signal  < 16):
        print("signal too week ,waiting... ")
        time.sleep(1)
        signal = getSignal()    

    serialSendMsg('AT+COPS=1,2,"46000"')    #//设置手动注册移动运营MNC
    serialSendMsg('AT+CSCON=1')             #//打开信号提示自动上报。
    serialSendMsg('AT+CGDCONT?')            # 打开注册信息自动上报
    serialSendMsg('AT+MIPLCREATE')
    serialSendMsg()

    return True 

def readMsg():
    with open('msg','r') as f:
        for i in f:
            pass    

