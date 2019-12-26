#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Installer le package Python 'RPi.GPIO' pour contrôler les sorties
# sudo python3 -m pip install pip --upgrade
# sudo python3 -m pip install rpi.gpio

import RPi.GPIO as GPIO
import time

# Choix du cablage selon la numérotation des GPIOs du SOC 'BCM'
GPIO.setmode(GPIO.BCM)

# Paramétrage des sorties
GPIO.setup(26,GPIO.OUT,initial=GPIO.LOW)

try:
   GPIO.output(26,GPIO.HIGH)

   # On attend encore un dizième de seconde et on arrête
   time.sleep(0.1)

   GPIO.output(26,GPIO.LOW)

except:
   print("stopping")

# Libération des ressources du module et éteint tout
GPIO.cleanup()
