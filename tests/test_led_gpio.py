#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

ledGRE_Pin = 22 # WiringPi header pin 3
ledYEL_Pin = 23 # WiringPi header pin 4
ledBLU_Pin = 24 # WiringPi header pin 5

# Choix du cablage selon la numérotation des GPIOs du SOC 'BCM'
GPIO.setmode(GPIO.BCM)

# Paramétrage des sorties
GPIO.setup( ledGRE_Pin, GPIO.OUT )
GPIO.setup( ledYEL_Pin, GPIO.OUT )
GPIO.setup( ledBLU_Pin, GPIO.OUT )

try:
   while True:
      print "LED GREEN *on*, LED YELLOW off, LED BLUE off"
      GPIO.output( ledGRE_Pin, GPIO.HIGH )
      GPIO.output( ledYEL_Pin, GPIO.LOW )
      GPIO.output( ledBLU_Pin, GPIO.LOW )

      # On attend une demi-seconde
      time.sleep( 0.5 )

      print "LED GREEN off, LED YELLOW *on*, LED BLUE off"
      GPIO.output( ledGRE_Pin, GPIO.LOW )
      GPIO.output( ledYEL_Pin, GPIO.HIGH )
      GPIO.output( ledBLU_Pin, GPIO.LOW )
 
       # On attend une demi-seconde
      time.sleep( 0.5 )

      print "LED GREEN off, LED YELLOW off, LED BLUE *on*"
      GPIO.output( ledGRE_Pin, GPIO.LOW )
      GPIO.output( ledYEL_Pin, GPIO.LOW )
      GPIO.output( ledBLU_Pin, GPIO.HIGH )

      # On attend encore une demi-seconde et on recommence
      time.sleep( 0.5 )

except:
      print "stopping"

# Libération des ressources du module
# (éteint tout)
GPIO.cleanup()
