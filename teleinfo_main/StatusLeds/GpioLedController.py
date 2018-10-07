# -*- coding: UTF-8 -*-

# Dépendances
import Debug  # Besoin de mon décorateur "call_log"
import RPi.GPIO as GPIO
import time


# *** Notes sur RPi.GPIO ***
# Nécessite sur le système : le package Python 'RPi.GPIO' pour contrôler les sorties
# sudo python3 -m pip install pip --upgrade
# sudo python3 -m pip install rpi.gpio


file = __file__.split('\\')[-1]


class GpioLedController:
    """
    Cette classe permet de controler facilement les 4 leds de statut du montage Télépi
    """

    # Montage 'telepi' sur PI T-clobber (V2.2)
    # Id des GPIO pour les 4 leds colorées
    GPIO_ID_LED_B = 17  # GPIO P0, led bleue
    GPIO_ID_LED_Y = 18  # GPIO P1, led jaune
    GPIO_ID_LED_G = 27  # GPIO P2, led verte
    GPIO_ID_LED_R = 22  # GPIO P3, led rouge

    # Liste des 4 leds
    leds = (GPIO_ID_LED_B, GPIO_ID_LED_Y, GPIO_ID_LED_G, GPIO_ID_LED_R)

    # Temporisation de maintien des leds
    TIMER_SECS = 0.4

    @Debug.call_log
    def __init__(self):
        # Choix du cablage selon la numérotation des GPIOs du SOC 'BCM'
        GPIO.setmode(GPIO.BCM)

        # Paramétrage des sorties
        for led in self.leds:
            GPIO.setup(led, GPIO.OUT)

    @Debug.call_log
    def set_off(self, led=None):
        """
        Une led donnée ou toutes les leds éteintes
        """
        if led is not None:
            if led in self.leds:
                GPIO.output(led, GPIO.LOW)
        else:
            for led in self.leds:
                GPIO.output(led, GPIO.LOW)

    @Debug.call_log
    def set_on(self, led=None):
        """
        Une led donnée ou toutes les leds allumées
        """
        if led is not None:
            if led in self.leds:
                GPIO.output(led, GPIO.HIGH)
        else:
            for led in self.leds:
                GPIO.output(led, GPIO.HIGH)

    @Debug.call_log
    def running_leds(self):
        """
        Chenillard sur les leds, à la fin toutes les leds sont éteintes
        """
        self.set_off()
        self.set_on()
        time.sleep(self.TIMER_SECS)
        self.set_off()

        # Dans un sens
        for i in range(0, len(self.leds)):
            print(i)
            GPIO.output(self.leds[i], GPIO.HIGH)
            time.sleep(self.TIMER_SECS)
            GPIO.output(self.leds[i], GPIO.LOW)

        time.sleep(self.TIMER_SECS)
        self.set_on()
        time.sleep(self.TIMER_SECS)
        self.set_off()
        time.sleep(self.TIMER_SECS)

        # Puis dans l'autre
        for i in range(len(self.leds)-1, -1, -1):
            print(i)
            GPIO.output(self.leds[i], GPIO.HIGH)
            time.sleep(self.TIMER_SECS)
            GPIO.output(self.leds[i], GPIO.LOW)

    @Debug.call_log
    def __enter__(self):
        print("...")

    @Debug.call_log
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.free()

    @Debug.call_log
    def __del__(self):
        print('...')
