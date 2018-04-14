#!/usr/bin/python
# coding: utf-8

# ========================================
# Programme de test des capteurs et du LCD
# ========================================


import lcd_lib
#import logging
#logging.basicConfig(level=logging.DEBUG)
import sys
import Adafruit_DHT
import Adafruit_BMP.BMP085 as Adafruit_BMP085
import Adafruit_BMP.BMP280 as Adafruit_BMP280
import Adafruit_BME280
import ds18b20_lib
import time

# On initialise le LCD
lcd = lcd_lib.lcd()
lcd.lcd_clear()
lcd.lcd_display_string("Sensing...",1)

print('DS18B20')
ds18b20_lib.read_temp_all()

print('AM2302')
lcd.lcd_clear()
lcd.lcd_display_string("AM2302",1)
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 5)

if humidity is not None and temperature is not None:
    print('Temperature={0:0.1f}°C\nHumidity={1:0.1f}%'.format(temperature, humidity))
    lcd.lcd_display_string("{0:0.1f}C {1:0.1f}%".format(temperature, humidity),2)
else:
    print('Failed!')
    sys.exit(1)

#print('BMP180')
#sst180 = Adafruit_BMP085.BMP085(mode=Adafruit_BMP085.BMP085_STANDARD, address=0x77)

#print('Temperature={0:0.2f}°C'.format(sst180.read_temperature()))
#print('Pressure={0:0.2f}Pa'.format(sst180.read_pressure()))
#print('Altitude={0:0.2f}m'.format(sst180.read_altitude()))

#print('BMP280')
#sst280p = Adafruit_BMP280.BMP280(address=0x76)

#print('Temperature={0:0.2f}°C'.format(sst280p.read_temperature()))
#print('Pressure={0:0.2f}Pa'.format(sst280p.read_pressure()))
#print('Altitude={0:0.2f}m'.format(sst280p.read_altitude()))

time.sleep(5)

lcd.lcd_clear()
lcd.lcd_display_string("Sensing...",1)

print('BME280')
sst280e = Adafruit_BME280.BME280(mode=Adafruit_BME280.BME280_OSAMPLE_8,address=0x77)

temperature = sst280e.read_temperature()
pressure = sst280e.read_pressure()/100
humidity = sst280e.read_humidity()

print 'Temperature={0:0.1f}°C'.format(temperature)
print 'Pressure={0:0.2f}hPa'.format(pressure)
print 'Humidity={0:0.1f}%'.format(humidity)

lcd.lcd_clear()
lcd.lcd_display_string("BME280: {0:0.2f}h".format(pressure),1)
lcd.lcd_display_string("{0:0.1f}C {1:0.1f}%".format(temperature, humidity),2)
