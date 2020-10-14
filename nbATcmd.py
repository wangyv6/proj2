from mUtils import serialSendMsg  ,readConf 
import time


AT_CMD = ["AT+CGREG?","AT+MIPLCREATE"]
def signalCallBack():
    print("signal too week")

def getSignal():  
    r""" 获得信号强度 """
    ret = serialSendMsg('AT+CSQ')
    
    return int(ret[1])



def initConnect():
    signal=   getSignal()   
    while(signal  < 16):
        print("signal too week ,waiting... ")
        time.sleep(1)
        signal = getSignal()    

    

