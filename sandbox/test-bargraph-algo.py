#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Montage 'telepi' avec Adafruit T-Clobber Plus
leds = (18, 23, 24, 17, 27, 22, 5, 6, 13, 19)


def indication(si, minv=0, maxv=10, v=5):
    """
    Indication de la mesure, allumage des leds proportionnellement à la mesure
    """
    s  = (maxv - minv) / len(leds)  # -- valeur associée à un pas du bargraph
    nb = v / s             # -- nombre de pas du bargraph à activer
    nb = round(min(nb, len(leds)))
    print('=>', v, maxv, len(leds), s, nb)

    active_leds = ()
    inactive_leds = ()

    for i in range(nb):
        active_leds += (leds[i],)

    for j in range(nb, len(leds)):
        inactive_leds += (leds[j],)

    print('ON: ', active_leds, len(active_leds))
    print('OFF:', inactive_leds, len(inactive_leds))


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
