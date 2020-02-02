#!/usr/bin/python
# -*- coding: UTF-8 -*-

# *** Dépendances ***
import StatusLeds
import Debug  # Besoin de mon décorateur "log_func"

"""
Quelques fonctions pour indiquer facilement l'état du système en utilisant les leds.
"""


@Debug.log_class_func
def running_leds(si):
    """
    Chenillard sur les leds de statut, à la fin toutes les leds sont éteintes
    """
    si.running_leds(si.status_leds)


@Debug.log_func
def presence(si):
    """
    LED bleue allumée, seule
    """
    si.set_off(si.status_leds)
    si.set_on(si.status_leds, StatusLeds.GpioLedController.GPIO_ID_LED_BLUE)


@Debug.log_func
def initialization_failed(si):
    """
    LED rouge et LED jaune allumées, seules
    """
    si.set_off(si.status_leds)
    si.set_on(si.status_leds, StatusLeds.GpioLedController.GPIO_ID_LED_RED)
    si.set_on(si.status_leds, StatusLeds.GpioLedController.GPIO_ID_LED_YELLOW)


@Debug.log_func
def initialized(si):
    """
    LED verte allumée, seule
    """
    si.set_off(si.status_leds)
    si.set_on(si.status_leds, StatusLeds.GpioLedController.GPIO_ID_LED_GREEN)


@Debug.log_func
def running(si):
    """
    LED blanche allumée puis éteinte
    """
    si.flash_led(si.status_leds, StatusLeds.GpioLedController.GPIO_ID_LED_WHITE)


@Debug.log_func
def aborted(si):
    """
    LED rouge allumée, seule
    """
    si.set_off()
    si.set_on(si.status_leds, StatusLeds.GpioLedController.GPIO_ID_LED_RED)
