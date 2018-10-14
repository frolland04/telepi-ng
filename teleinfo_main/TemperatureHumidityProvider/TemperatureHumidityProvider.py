# -*- coding: UTF-8 -*-

# Dépendances
import threading
import datetime

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
        self.__pressure = 0.0

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

        val, ok = self.readRelativeHumidity()
        if ok:
            self.__humidity = val

        # val, ok = self.readTemperature()
        # if ok:
        #     self.__temperature = val
        #
        # val, ok = self.readAirPressure()
        # if ok:
        #     self.__pressure = val

        if not self.end:
            # On relance pour une prochaine occurrence
            self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
            self.t.start()

    def readRelativeHumidity(self):
        """Lecture de l'humidité relative depuis le BME280 et mise à jour des compteurs de BDD"""

        # Mise à jour des compteurs
        self.ex.pool.incrementCountEnvRelativeHumidityNbReadTotal()
        self.ex.pool.setCountEnvRelativeHumidityReadLastTs(datetime.datetime.now())

        # Lecture depuis le BME280
        val = self.BME280_I2C.humidity
        print('DBG_ENV: Humidity', '{:.0f}'.format(self.val))

        # Les valeurs sont-elles dans des plages raisonnables?
        if val <= 0.0 or val >= 100:
            self.ex.pool.incrementCountEnvRelativeHumidityNbReadInvalid()
            ok = False
        else:
            # Oui, on valide la nouvelle prise de mesure
            self.ex.pool.incrementCountEnvRelativeHumidityNbReadOk()
            ok = True

        return val, ok

    def readTemperature(self):
        """Lecture de la température depuis le BME280 et mise à jour des compteurs de BDD"""

        # Mise à jour des compteurs
        self.ex.pool.incrementCountEnvTemperatureNbReadTotal()
        self.ex.pool.setCountEnvTemperatureReadLastTs(datetime.datetime.now())

        val = 0.0
        ok = False

        try:
            # Lecture depuis le BME280
            val = self.BME280_I2C.temperature
            print('DBG_ENV: Temperature', '{:.1f}'.format(self.val))

            # Les valeurs sont-elles dans des plages raisonnables?
            if val <= -20.0 or val >= 60:
                self.ex.pool.incrementCountEnvTemperatureNbReadInvalid()
                ok = False
            else:
                # Oui, on valide la nouvelle prise de mesure
                self.ex.pool.incrementCountEnvTemperatureNbReadOk()
                ok = True
        except:
            self.ex.pool.incrementCountEnvTemperatureNbReadFailed()
            ok = False

        return val, ok
    
    def readAirPressure(self):
        """Lecture de la pression atmosphérique depuis le BME280 et mise à jour des compteurs de BDD"""

        # Mise à jour des compteurs
        self.ex.pool.incrementCountEnvAirPressureNbReadTotal()
        self.ex.pool.setCountEnvAirPressureReadLastTs(datetime.datetime.now())

        val = 0.0
        ok = False

        try:
            # Lecture depuis le BME280
            val = self.BME280_I2C.pressure
            print('DBG_ENV: Pression Atmosphérique', '{:.2f}'.format(self.val))

            # On valide la nouvelle prise de mesure
            self.ex.pool.incrementCountEnvAirPressureNbReadOk()
            ok = True

        except:
            self.ex.pool.incrementCountEnvAirPressureNbReadFailed()
            ok = False

        return val, ok

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

    @property
    def pressure(self):
        """Je suis une @propriété Python."""
        print("TemperatureHumidityProvider.pressure@get")
        return self.__pressure

    @Debug.call_log
    def __enter__(self):
        print('...')

    @Debug.call_log
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @Debug.call_log
    def __del__(self):
        print('...')
