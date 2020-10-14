
import json
import os
import time
import serial

import json

configMsg = []


class serialConfig:
    def __init__(self) -> None:
        self.baudrate = 9600
        self.devicePath = '/dev/ttyUSB0'  # 一般是这样 也可能是USB1

# 读取配置文件
def readConf(configPath="config.json"):
    r""" 读取配置文件
        configPath 文件绝对路径
     """
    data = []
    with open("config.json", "r")as f:
        data = json.load(f)

    configMsg = data
    return configMsg


# 调试用 ，也可以生成配置文件
def saveConf(configPath="config.json"):
    r""" 保存配置文件
        手动重置配置文件，调试用
    """
    data = {
        "isDbg": True,          # 是否是调试状态
        "isLockEs": False,
        "confFileName": configPath,  # 文件保存位置
        "devs": {                    # 单个传感器配置信息
            "sim7020c": {
                "path": "/dev/ttyUSB0",
                "bps": 9600,
                "stopbit": 1,
                "parity": 0,
            },
            "dht11": {
                "outPin": 0
            }
        }

    }
    # data = json.loads(str(data).encode("utf8"))
    with open(configPath, 'w') as f:
        json.dump(data, f)


# 获取串口
def getSerial(port='/dev/ttyUSB0',
                 baudrate=115200,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE,
                 bytesize=serial.EIGHTBITS):
    r""" 获取配置好的串口 ，返回串口se"""
    se = serial.Serial(port=port, baudrate=baudrate,
                       parity=parity, stopbits=stopbits, bytesize=bytesize)

    return se
# infor



def serialSendMsg( Msg,ser ):
    r""" 通用信息发送 """
    msg = Msg+'\r\r\n'
    ser.write(msg.encode('ascii'))
    time.sleep(0.2) # 必要的等待时间 
    retMsg = ser.read_all().decode('ascii')[len(msg):].split('\r\n')
    retMsg = [i for i in retMsg   if len(i)!=0 ]
    # print(retMsg)
    return retMsg   


if __name__ == "__main__":

    # saveConf()
    # cfg = readConf()
    # print(cfg)
    # serialcfg  = cfg['devs']['sim7020c']
    # print(serialcfg)
    se  =getSerial()
    msg = serialSendMsg("AT",se)
    print(msg)
    pass
