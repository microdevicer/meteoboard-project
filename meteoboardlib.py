#
# library for MeteoBoard
# v.0.1

import os
import serial
from serial.tools import list_ports
import time

import re


def list_serial_ports():
    # Windows
    if os.name == 'nt':
        # Scan for available ports.
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append('COM'+str(i + 1))
                s.close()
            except serial.SerialException:
                pass
        return available
    else:
        # Mac / Linux
        return [port[0] for port in list_ports.comports()]


def meteoboard_port(available_ports_list):
    str = ''
    device_cport = ''
    j=0
    for i in range (len(available_ports_list)):
        try:
            s = serial.Serial(available_ports_list[i], timeout = 0.01)
            s.write("w")
            str = s.read(20)
            if str == 'MeteoBoard':
                s.flushInput()
                j+=1
                device_port = available_ports_list[i]                
            s.close()
        except serial.SerialException:
             pass
    if j == 0:
        device_port = 'NaN'
    return device_port
        
def getMeteoBoard_port():
    return meteoboard_port(list_serial_ports())     
      
        
def getDHT11_temp(port):
    tmp =''
    temp = 0
    pattern = '\S+'
    
    ser = serial.Serial(port, 19200, timeout=0.2) #open 
    ser.write(chr(4) + chr(1) + chr(10)) #write
    tmp = ser.read(20) #read
    found = re.findall(pattern, tmp)
    ser.close() #close

    if found[0] == '4' and found[1] == '1':
        temp = int(found[2])
    else:
        temp = 0
    return temp

def getDHT11_Hum(port):
    tmp =''
    temp = 0
    pattern = '\S+'
    
    ser = serial.Serial(port, 19200, timeout=0.2) #open 
    ser.write(chr(4) + chr(2) + chr(10)) #write
    tmp = ser.read(20) #read
    found = re.findall(pattern, tmp)
    ser.close() #close

    if found[0] == '4' and found[1] == '2':
        temp = int(found[2])
    else:
        temp = 0
    return temp
    
def getDS18b20_temp_1(port):
    tmp =''
    temp = 0
    pattern = '\S+'
    
    ser = serial.Serial(port, 19200, timeout=0.2) #open 
    ser.write(chr(1) + chr(1) + chr(10)) #write
    tmp = ser.read(20) #read
    found = re.findall(pattern, tmp)
    ser.close() #close

    if found[0] == '1' and found[1] == '1':
        temp = int(found[2])
    else:
        temp = 0
    return temp

def getDS18b20_temp_2(port):
    tmp =''
    temp = 0
    pattern = '\S+'
    
    ser = serial.Serial(port, 19200, timeout=0.2) #open 
    ser.write(chr(2) + chr(1) + chr(10)) #write
    tmp = ser.read(20) #read
    found = re.findall(pattern, tmp)
    ser.close() #close

    if found[0] == '2' and found[1] == '1':
        temp = int(found[2])
    else:
        temp = 0
    return temp
    
def getDS18b20_temp_3(port):
    tmp =''
    temp = 0
    pattern = '\S+'
    
    ser = serial.Serial(port, 19200, timeout=0.2) #open 
    ser.write(chr(3) + chr(1) + chr(10)) #write
    tmp = ser.read(20) #read
    found = re.findall(pattern, tmp)
    ser.close() #close

    if found[0] == '3' and found[1] == '1':
        temp = int(found[2])
    else:
        temp = 0
    return temp

def getBMP085_temp(port):
    tmp =''
    temp = 0
    pattern = '\S+'
    
    ser = serial.Serial(port, 19200, timeout=0.2) #open 
    ser.write(chr(5) + chr(1) + chr(10)) #write
    tmp = ser.read(20) #read
    found = re.findall(pattern, tmp)
    ser.close() #close

    if found[0] == '5' and found[1] == '1':
        temp = int(found[2])
    else:
        temp = 0
    return temp

def getBMP085_pressure(port):
    tmp =''
    temp = 0
    pattern = '\S+'
    
    ser = serial.Serial(port, 19200, timeout=0.2) #open 
    ser.write(chr(5) + chr(3) + chr(10)) #write
    tmp = ser.read(20) #read
    found = re.findall(pattern, tmp)
    ser.close() #close

    if found[0] == '5' and found[1] == '3':
        temp = int(found[2])
    else:
        temp = 0
    return temp
    

def getBMP085_altitude(port):
    tmp =''
    temp = 0
    pattern = '\S+'
    
    ser = serial.Serial(port, 19200, timeout=0.2) #open 
    ser.write(chr(5) + chr(4) + chr(10)) #write
    tmp = ser.read(20) #read
    found = re.findall(pattern, tmp)
    ser.close() #close

    if found[0] == '5' and found[1] == '4':
        temp = int(found[2])
    else:
        temp = 0
    return temp
    
