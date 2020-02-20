#!/usr/bin/python
# -*- coding: UTF-8 -*-

# *** Sous-modules ***
import StatusLeds
import Debug  # Besoin de mon décorateur "log_func"

"""
Quelques fonctions pour manipuler facilement les leds du bargraph
"""


@Debug.log_func
def running_leds(si):
    """
    Chenillard sur les leds du bargraph, à la fin toutes les leds sont éteintes
    """
    si.running_leds(si.bargraph_leds)


@Debug.log_func
def indication(si, min=0, max=10, v=0):
    """
    Indication de la mesure, allumage des leds proportionnellement à la mesure
    """
    si.set_off(si.bargraph_leds)
