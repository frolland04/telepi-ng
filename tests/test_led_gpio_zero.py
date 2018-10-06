#!/usr/bin/env python3
# coding: utf-8

# ==========================
# Programme de test GPIO LED
# ==========================

from gpiozero import LED
import time

if __name__ == '__main__':
    led = LED(17)
    led.on()
    time.sleep(2)


