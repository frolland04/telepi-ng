#!/usr/bin/env python3
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

# On affiche des caractères sur chaque ligne (16x2 ou 4x20)
big = True

if big:
   # Avec le grand écran
   lcd.lcd_display_string("12345678901234567890", 1)
   lcd.lcd_display_string("ABCDEFGHIJKLMNOPQRST", 2)
   lcd.lcd_display_string("abcdefghijklmnopqrst", 3)
   lcd.lcd_display_string("12345678901234567890", 4)
else:
   # Sinon avec le petit
   lcd.lcd_display_string("1234567890123456", 1)
   lcd.lcd_display_string("ABCDEFGHIJKLMNOP", 2)
