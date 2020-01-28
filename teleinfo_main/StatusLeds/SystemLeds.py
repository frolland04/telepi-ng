#!/usr/bin/python
# -*- coding: UTF-8 -*-

# *** Dépendances ***
import StatusLeds
import Debug  # Besoin de mon décorateur "call_log"


"""
Quelques fonctions pour indiquer facilement l'état du système en utilisant les leds.
"""


@Debug.call_log
def presence(si):
    """LED bleue allumée, seule"""
    si.set_off()
    si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_BLUE)


@Debug.call_log
def initialization_failed(si):
    """LED rouge et LED jaune allumées, seules"""
    si.set_off()
    si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_RED)
    si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_YELLOW)


@Debug.call_log
def initialized(si):
    """LED verte allumée, seule"""
    si.set_off()
    si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_GREEN)


@Debug.call_log
def running(si):
    """LED blanche allumée puis éteinte"""
    si.flash_led(StatusLeds.GpioLedController.GPIO_ID_LED_WHITE)


@Debug.call_log
def aborted(si):
    """LED rouge allumée, seule"""
    si.set_off()
    si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_RED)