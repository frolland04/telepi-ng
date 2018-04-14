#!/bin/bash
echo "--------- BMP180 on I2C bus '1' at '0x77' ---------"
python adf-libs/Adafruit_Python_BMP/examples/simpletest.py

echo "--------- AM2302 on GPIO #5 ---------"
python adf-libs/Adafruit_Python_DHT/examples/AdafruitDHT.py 2302 5
