#!/usr/bin/env python3
# coding: utf-8

# =============================================
# Programme de test du capteur Bosch SST BME280
# =============================================

# ```
# sudo python3 -m pip install setuptools --upgrade
# sudo pip3 install adafruit-circuitpython-bme280
# ```

import board
import digitalio
import busio
import adafruit_bme280

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

if __name__ == '__main__':
    print("Temperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
 
