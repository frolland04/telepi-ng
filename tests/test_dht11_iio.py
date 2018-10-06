#!/bin/bash

IIO_FILE_AM2302_T="/sys/bus/iio/devices/iio:device0/in_temp_input"
IIO_FILE_AM2302_H="/sys/bus/iio/devices/iio:device0/in_humidityrelative_input"

while true  
do
echo "Lecture"
echo `cat $IIO_FILE_AM2302_T`
echo `cat $IIO_FILE_AM2302_H`

sleep 2
done



