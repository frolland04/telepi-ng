#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dépendances
import serial

file = __file__.split('\\')[-1]

# Port série utilisé
MESSAGE_PORT_NAME = '/dev/ttyAMA0'

# Ouverture du port série
print(file + ':', 'MESSAGE_PORT_NAME=' + MESSAGE_PORT_NAME)

si = serial.Serial(
    port=MESSAGE_PORT_NAME,
    baudrate=1200,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)

si.flushInput()

# Lecture de tout ce qui arrive par le port série
while True:
    print(si.read(1).decode(), end='')


