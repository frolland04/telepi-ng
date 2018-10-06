#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Installer le package Python 'RPi.GPIO' pour contrôler les sorties
# sudo python3 -m pip install pip --upgrade
# sudo python3 -m pip install rpi.gpio

import RPi.GPIO as GPIO
import time

# Montage 'telepi' sur PI T-clobber (V2.2)
led_BLEU  = 17  # GPIO P0
led_JAUNE = 18  # GPIO P1
led_VERTE = 27  # GPIO P2
led_ROUGE = 22  # GPIO P3

ledPin = led_VERTE

#Choix du cablage selon la numérotation des GPIOs du SOC 'BCM'
GPIO.setmode(GPIO.BCM)

# Paramétrage des sorties
GPIO.setup( ledPin, GPIO.OUT )

try:
   while True:
      print("LED *on*")
      GPIO.output( ledPin, GPIO.HIGH )

      # On attend une demi-seconde
      time.sleep( 0.5 )

      print("LED off")
      GPIO.output( ledPin, GPIO.LOW )
       
      # On attend encore une demi-seconde et on recommence
      time.sleep( 0.5 )

except:
      print ("stopping")

# Libération des ressources du module
# (et éteint tout)
GPIO.cleanup()
