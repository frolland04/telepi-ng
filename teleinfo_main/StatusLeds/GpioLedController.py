# -*- coding: UTF-8 -*-

# Dépendances
import RPi.GPIO as GPIO
import time

# *** Notes sur RPi.GPIO ***
# Nécessite sur le système : le package Python 'RPi.GPIO' pour contrôler les sorties
# sudo python3 -m pip install pip --upgrade
# sudo python3 -m pip install rpi.gpio

# Sous-modules
import Debug  # Besoin de mon décorateur "log_class_func" & "EnterExitLogger"

# Pour le débogage
this_file = __file__.split('\\')[-1]


class GpioLedController:
    """
    Cette classe permet de contrôler facilement les 5 leds de statut du montage Télépi
    ainsi que le bargraph de 10 leds
    """

    # Montage 'télépi' sur PI AdaFruit T-Clobber Plus
    # -----------------------------------------------

    # Identités des GPIOs pour les 5 leds colorées
    GPIO_ID_LED_BLUE = 25
    GPIO_ID_LED_GREEN = 12
    GPIO_ID_LED_YELLOW = 16
    GPIO_ID_LED_RED = 20
    GPIO_ID_LED_WHITE = 21

    # Liste des 5 leds colorées, dans l'ordre d'apparition sur le montage 'télépi'
    status_leds = (GPIO_ID_LED_BLUE, GPIO_ID_LED_GREEN, GPIO_ID_LED_YELLOW, GPIO_ID_LED_RED, GPIO_ID_LED_WHITE)

    # Identités des GPIOs pour les sorties qui correspondent au bargraph (10 leds colorées)
    # également dans l'ordre d'apparition
    bargraph_leds = (18, 23, 24, 17, 27, 22, 5, 6, 13, 19)

    # Temporisation de maintien des leds
    LED_HOLDON_TIMER_SECS = 0.4

    @Debug.log_class_func
    def __init__(self):
        """
        Initialisation du 'GpioLedController' : ressources GPIO
        """
        # Choix du câblage selon la numérotation des GPIOs du SOC 'BCM'
        GPIO.setmode(GPIO.BCM)

        # Paramétrage des sorties et effacement
        for led in self.status_leds:
            GPIO.setup(led, GPIO.OUT)
            GPIO.output(led, GPIO.LOW)
        for led in self.bargraph_leds:
            GPIO.setup(led, GPIO.OUT)
            GPIO.output(led, GPIO.LOW)

        # On veut déboguer les entrées/sorties de contexte d'exécution
        self.ct = Debug.EnterExitLogger()

    @Debug.log_class_func
    def __del__(self):
        """
        Nettoyage du 'GpioLedController'
        """
        print('...')

    @Debug.log_class_func
    def close(self):
        """
        Fin propre du 'GpioLedController' : libération des ressources GPIO
        """
        GPIO.cleanup()

    @Debug.log_class_func
    def set_off(self, leds, led=None):
        """
        Une led donnée ou toutes les leds éteintes.
        Travaille sur la liste de leds données en paramètre.
        """
        if led is not None:
            if led in leds:
                GPIO.output(led, GPIO.LOW)
        else:
            for led in leds:
                GPIO.output(led, GPIO.LOW)

    @Debug.log_class_func
    def set_on(self, leds, led=None):
        """
        Une led donnée ou toutes les leds allumées.
        Travaille sur la liste de leds données en paramètre.
        """
        if led is not None:
            if led in leds:
                GPIO.output(led, GPIO.HIGH)
        else:
            for led in leds:
                GPIO.output(led, GPIO.HIGH)

    @Debug.log_class_func
    def flash_led(self, leds, led=None):
        """
        Un flash avec la led donnée ou toutes les leds allumées, à la fin toutes les leds sont éteintes.
        Travaille sur la liste de leds données en paramètre.
        """
        if (led is not None and led in leds) or led is None:
            self.set_off(leds, led)
            time.sleep(self.LED_HOLDON_TIMER_SECS)
            self.set_on(leds, led)
            time.sleep(self.LED_HOLDON_TIMER_SECS)
            self.set_off(leds, led)
            time.sleep(self.LED_HOLDON_TIMER_SECS)

    @Debug.log_class_func
    def running_leds(self, leds):
        """
        Chenillard sur les leds, à la fin toutes les leds sont éteintes.
        Travaille sur la liste de leds données en paramètre.
        """
        # Un premier "flash" de toutes les leds ensemble
        self.flash_led(leds)

        # Le chenillard dans un sens
        for i in range(0, len(leds)):
            print(i+1, '/', len(leds))
            GPIO.output(leds[i], GPIO.HIGH)
            time.sleep(self.LED_HOLDON_TIMER_SECS)
            GPIO.output(leds[i], GPIO.LOW)

        # Un second "flash" de toutes les leds ensemble
        self.flash_led(leds)

        # Le chenillard dans l'autre sens
        for i in range(len(leds) - 1, -1, -1):
            print(i+1, '/', len(leds))
            GPIO.output(leds[i], GPIO.HIGH)
            time.sleep(self.LED_HOLDON_TIMER_SECS)
            GPIO.output(leds[i], GPIO.LOW)

    @Debug.log_class_func
    def __enter__(self):
        """
        Entrée de zone de portée, pour gestion de contextes
        """
        print("...")
        self.ct.__enter__()
        return self

    @Debug.log_class_func
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Sortie de zone de portée, pour gestion de contextes
        """
        print("...")
        return self.ct.__exit__(exc_type, exc_val, exc_tb)
