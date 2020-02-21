#!/usr/bin/python
# -*- coding: UTF-8 -*-

# *** Sous-modules ***
import Debug  # Besoin de mon décorateur "log_func"


def dbg_msg(*args):
    """
    Hook to print (or not) debugging messages for this Python file.
    """
    print('[DBG]', *args)


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
def indication(si, minv=0, maxv=10, v=5):
    """
    Indication de la mesure, allumage des leds proportionnellement à la mesure
    """
    s  = (maxv - minv) / len(si.bargraph_leds)  # -- valeur associée à un pas du bargraph
    nb = v / s  # -- nombre de pas du bargraph à activer
    nb = round(min(nb, len(si.bargraph_leds)))
    dbg_msg('BARGRAPH_INFO:', v, maxv, len(si.bargraph_leds), s, nb)

    # On allume une partie des leds
    active_leds = ()
    for i in range(nb):
        active_leds += (si.bargraph_leds[i],)

    dbg_msg('ON: ', active_leds, len(active_leds))
    si.set_on(active_leds)

    # On éteint une autre partie des leds
    inactive_leds = ()
    for j in range(nb, len(leds)):
        inactive_leds += (si.bargraph_leds[j],)
    
    dbg_msg('OFF:', inactive_leds, len(inactive_leds))
    si.set_off(inactive_leds)


# Pour essayer les fonctions de ce fichier Python.
# ------------------------------------------------

if __name__ == "__main__":
    print('COUCOU!')

    indication(None, 0, 11000, 400)

    indication(None, 0, 11000, 850)

    indication(None, 0, 11000, 1120)

    indication(None, 0, 11000, 3500)

    indication(None, 0, 11000, 7500)

    indication(None, 0, 11000, 9000)

    indication(None, 0, 11000, 10400)

    indication(None, 0, 11000, 14850)

    print('ByeBye!')
