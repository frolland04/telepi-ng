#!/usr/bin/python
# coding: utf-8

# ========================
# Programme de test du LCD
# ========================


# On importe le pilote
import sys
import lcd_lib
from time import *

# On initialise le LCD
lcd = lcd_lib.lcd()

# On efface
lcd.lcd_clear()

# On affiche des caracteres sur chaque ligne
lcd.lcd_display_string("Hello", 1)
lcd.lcd_display_string("World !", 2)
