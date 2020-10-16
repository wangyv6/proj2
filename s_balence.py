

from mUtils import getSerial, writeSensorMsg, serialSendMsg


def getBalence(ser,isWriteData, id,hasSerial =False,):
    ser = getSerial()
    ser = ser
    ATcmd = ''
    ret = serialSendMsg(ATcmd,ser=ser)
    writeSensorMsg(id, msgType='b', msg=ret)
    return ret
