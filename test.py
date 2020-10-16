#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from mUtils import serialSendMsg,getSerial
import serial as se 
import time

se = getSerial()
retmsg = serialSendMsg('AT+CPIN?',ser=se)




print(retmsg)