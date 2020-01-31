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
import Debug  # Besoin de mon décorateur "log_class_func" & "EnterExitLogger"

# Pour le débogage
this_file = __file__.split('\\')[-1]


class TemperatureHumidityProvider:
    """
    Une classe de mesure de l'environnement proche : température et humidité
    Communique avec un capteur Bosch SST BME 280 à l'aide de la librairie CircuitPython
    """

    # Une mesure toutes les 20s
    TIMER_PERIOD_SECS = 20

    @Debug.log_class_func
    def __init__(self, ex):
        """
        Initialisation du 'TemperatureHumidityProvider' : données, communication avec le capteur, timer
        """
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

        # On veut déboguer les entrées/sorties de contexte d'exécution
        self.ct = Debug.EnterExitLogger()

    @Debug.log_class_func
    def __del__(self):
        """
        Nettoyage du 'TemperatureHumidityProvider'
        """
        print('...')

    @Debug.log_class_func
    def close(self):
        """
        Fin propre du 'TemperatureHumidityProvider' : arrêt timer si en attente et pas de relance
        si en cours d'exécution, grâce à condition d'arrêt
        """
        # On signale l'arrêt
        self.end = True

        # On annule le timer
        self.t.cancel()

    @Debug.log_class_func
    def run(self):
        """
        Corps du timer : traitement exécuté périodiquement
        """
        print("** Mesures de l'environnement **")

        val, ok = self.readRelativeHumidity()
        if ok:
            self.__humidity = val

        val, ok = self.readTemperature()
        if ok:
            self.__temperature = val

        val, ok = self.readAirPressure()
        if ok:
            self.__pressure = val

        if not self.end:
            # On relance pour une prochaine occurrence
            self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
            self.t.start()

    def readRelativeHumidity(self):
        """
        Lecture de l'humidité relative depuis le BME280 et mise à jour des compteurs de BDD
        """
        val = 0.0
        ok = False
        ts = datetime.datetime.now()

        # Mise à jour des compteurs BDD
        self.ex.pool.incrementCountEnvRelativeHumidityNbReadTotal()
        self.ex.pool.setCountEnvRelativeHumidityReadLastTs(ts)

        try:
            # Lecture depuis le BME280, avec une décimale conservée
            val = round(self.BME280_I2C.humidity, 1)
            print('DBG_ENV: RH', '{:.2f}'.format(val))

        except Exception as e:
            Debug.log_exc(e, this_file)
            self.ex.pool.incrementCountEnvRelativeHumidityNbReadFailed()

        else:
            # Les valeurs sont-elles dans des plages raisonnables?
            if val <= 0.0 or val >= 100:
                # Non, on la laissera de coté
                ok = False

                # Mise à jour des compteurs BDD
                self.ex.pool.incrementCountEnvRelativeHumidityNbReadInvalid()

            else:
                # Oui, on conserve la nouvelle mesure
                ok = True

                # Mise à jour des compteurs BDD
                self.ex.pool.incrementCountEnvRelativeHumidityNbReadOk()

                # Mise à jour valeur instantanée dans la BDD
                self.ex.pool.updateRhInst(val, ts)

        return val, ok

    def readTemperature(self):
        """
        Lecture de la température depuis le BME280 et mise à jour des compteurs de BDD
        """
        val = 0.0
        ok = False
        ts = datetime.datetime.now()

        # Mise à jour des compteurs BDD
        self.ex.pool.incrementCountEnvTemperatureNbReadTotal()
        self.ex.pool.setCountEnvTemperatureReadLastTs(ts)

        try:
            # Lecture depuis le BME280, avec une décimale conservée
            val = round(self.BME280_I2C.temperature, 1)
            print('DBG_ENV: TEMP', '{:.2f}'.format(val))

        except Exception as e:
            Debug.log_exc(e, this_file)
            self.ex.pool.incrementCountEnvTemperatureNbReadFailed()

        else:
            # Les valeurs sont-elles dans des plages raisonnables?
            if val <= -20.0 or val >= 60:
                # Non, on la laissera de coté
                ok = False

                # Mise à jour des compteurs BDD
                self.ex.pool.incrementCountEnvTemperatureNbReadInvalid()

            else:
                # Oui, on conserve la nouvelle mesure
                ok = True

                # Mise à jour des compteurs BDD
                self.ex.pool.incrementCountEnvTemperatureNbReadOk()

                # Mise à jour valeur instantanée dans la BDD
                self.ex.pool.updateTempInst(val, ts)

        return val, ok

    def readAirPressure(self):
        """
        Lecture de la pression atmosphérique depuis le BME280 et mise à jour des compteurs de BDD
        """
        val = 0.0
        ok = False
        ts = datetime.datetime.now()

        # Mise à jour des compteurs
        self.ex.pool.incrementCountEnvAirPressureNbReadTotal()
        self.ex.pool.setCountEnvAirPressureReadLastTs(ts)

        try:
            # Lecture depuis le BME280, avec deux décimales conservées
            val = round(self.BME280_I2C.pressure, 2)
            print('DBG_ENV: PA', '{:.2f}'.format(val))

        except Exception as e:
            Debug.log_exc(e, this_file)
            self.ex.pool.incrementCountEnvAirPressureNbReadFailed()

        else:
            # On conserve la nouvelle mesure
            ok = True

            # Mise à jour des compteurs BDD
            self.ex.pool.incrementCountEnvAirPressureNbReadOk()

            # Mise à jour valeur instantanée dans la BDD
            self.ex.pool.updatePaInst(val, ts)

        return val, ok

    @property
    def humidity(self):
        """
        Je suis une @propriété Python en lecture.
        """
        print("@TemperatureHumidityProvider.humidity")
        return self.__humidity

    @property
    def temperature(self):
        """
        Je suis une @propriété Python en lecture.
        """
        print("@TemperatureHumidityProvider.temperature")
        return self.__temperature

    @property
    def pressure(self):
        """
        Je suis une @propriété Python en lecture.
        """
        print("@TemperatureHumidityProvider.pressure")
        return self.__pressure

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
