# -*- coding: UTF-8 -*-

# Dépendances
import threading

# *** Notes sur board, digitalio, busio et adafruit_bme280 ***
# *** Nécessite ADAFRUIT CircuitPython Library for BME 280 ***
# sudo python3 -m pip install setuptools --upgrade
# sudo pip3 install adafruit-circuitpython-bme280

import board
import digitalio
import busio
import adafruit_bme280


# Sous-modules
import Debug


fileName = __file__.split('\\')[-1]


class TemperatureHumidityProvider:
    """
    Une classe de mesure de l'environnement proche : température et humidité
    Communique avec un capteur Bosch SST BME 280 à l'aide de la librairie CircuitPython
    """

    # Une mesure toutes les 20s
    TIMER_PERIOD_SECS = 20

    @Debug.call_log
    def __init__(self, ex):
        # Handle pour exécuter les requêtes à la BDD
        self.ex = ex

        # Dernières mesures
        self.__humidity = 0.0
        self.__temperature = 0.0

        # Préparation de l'accès au capteur Bosch SST BME280 par I2C
        # Selon montage télépi : BME280 I2C @=77 (3.3V)
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.BME280_I2C = adafruit_bme280.Adafruit_BME280_I2C(self.i2c)

        # Timer de déclenchement des mesures et condition d'arrêt
        self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
        self.end = False
        self.t.start()

    @Debug.call_log
    def close(self):
        """
        Fin propre : arrêt timer si en attente et pas de relance si en cours d'exécution
        grâce à condition d'arrêt
        """
        self.end = True
        self.t.cancel()

    @Debug.call_log
    def run(self):
        print("** Mesure de l'environnement **")

        self.__humidity = self.BME280_I2C.humidity
        self.__temperature = self.BME280_I2C.temperature

        if not self.end:
            # On relance pour une prochaine occurrence
            self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
            self.t.start()

    @property
    def humidity(self):
        """Je suis une @propriété Python."""
        print("TemperatureHumidityProvider.humidity@get")
        return self.__humidity

    @property
    def temperature(self):
        """Je suis une @propriété Python."""
        print("TemperatureHumidityProvider.temperature@get")
        return self.__temperature

    @Debug.call_log
    def __enter__(self):
        print('...')

    @Debug.call_log
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @Debug.call_log
    def __del__(self):
        print('...')
