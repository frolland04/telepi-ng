#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Installer le package Python 'RPi.GPIO' pour contrôler les sorties
# sudo python3 -m pip install pip --upgrade
# sudo python3 -m pip install rpi.gpio

import RPi.GPIO as GPIO
import time

# Montage 'telepi' avec Adafruit T-Clobber Plus 
leds = (18, 23, 24, 17, 27, 22, 5, 6, 13, 19)

# Choix du cablage selon la numérotation des GPIOs du SOC 'BCM'
GPIO.setmode(GPIO.BCM)

# Paramétrage des sorties
for gpio_id in leds:
    GPIO.setup( gpio_id, GPIO.OUT )
    GPIO.output( gpio_id, GPIO.LOW )

try:

   while True:

      # On commence au début de la liste des leds
      i = 0

      while i < len(leds):

         print(i)

         # On allume
         GPIO.output( leds[i], GPIO.HIGH )

         # On attend un dixième de seconde
         time.sleep( 0.1 )

         # On éteint
         GPIO.output( leds[i], GPIO.LOW )

         # On attend encore un dixième de seconde et on continue
         time.sleep( 0.1 )

         # Led suivante
         i = i+1

except:
      print ("stopping")

# Libération des ressources du module
# (et éteint tout)
GPIO.cleanup()
