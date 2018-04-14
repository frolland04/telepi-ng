#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

ledYel_Pin = 20
ledRed_Pin = 21

# Choix du cablage selon la numérotation des GPIOs du SOC 'BCM'
GPIO.setmode(GPIO.BCM)

# Paramétrage des sorties
GPIO.setup( ledYel_Pin, GPIO.OUT )
GPIO.setup( ledRed_Pin, GPIO.OUT )

try:
   while True:
      print "LED YELLOW on, LED RED off"
      GPIO.output( ledYel_Pin, GPIO.HIGH )
      GPIO.output( ledRed_Pin, GPIO.LOW )

      # On attend une seconde
      time.sleep( 1 )

      print "LED YELLOW off, LED RED on"
      GPIO.output( ledYel_Pin, GPIO.LOW )
      GPIO.output( ledRed_Pin, GPIO.HIGH )

      # On attend encore une seconde et on recommence
      time.sleep( 1 )

except:
      print "stopping"

# Libération des ressources du module
# (éteint tout)
GPIO.cleanup()
