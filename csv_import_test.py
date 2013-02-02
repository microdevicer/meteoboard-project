# -*- coding: UTF-8 -*-

from meteoboardlib import *
import csv

c = csv.writer(open("MYFILE.csv", "wb"))    
port = getMeteoBoard_port() # узнаем к какому порту подключена плата
    
#print str(getDHT11_Hum(port)) +' '+ str(getDHT11_temp(port)) + ' '+ str(getBMP085_temp(port)) + ' '+ str(getBMP085_pressure(port)) + ' '+ str(getBMP085_altitude(port))

#print u'Влажность, % = ', getDHT11_temp(port)
#print u'Температура, C = ',getDHT11_Hum(port)
#print u'Температура, C = ',getBMP085_temp(port)
#print u'Давление, Па = ',getBMP085_pressure(port)
#print u'Альтитуда, м = ',getBMP085_altitude(port)

c.writerow(["humidity,% ","Temperature,C ","Temperature,C ","Pressure,Pa ","altitude,m"])

for i in range(500):
    print i
    c.writerow([str(getDHT11_temp(port)),str(getDHT11_Hum(port)),str(getBMP085_temp(port)),str(getBMP085_pressure(port)), str(getBMP085_altitude(port))])
    
