#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Installer le package Python 'RPi.GPIO' pour contrôler les sorties
# sudo python3 -m pip install pip --upgrade
# sudo python3 -m pip install rpi.gpio

import RPi.GPIO as GPIO
import time

# Choix du cablage selon la numérotation des GPIOs du SOC 'BCM'
GPIO.setmode(GPIO.BCM)

# Paramétrage des entrées
# GPIO 4 : si l'entrée n'est pas branchée, on tire son état à 'HAUT' (1), si on ferme le circuit à la masse on obtient 'BAS' (0)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
   while True:

      print('4',GPIO.input(4))

      # On attend encore une demi-seconde et on recommence
      time.sleep(0.5)

except:
      print ("stopping")

# Libération des ressources du module et éteint tout
GPIO.cleanup()
