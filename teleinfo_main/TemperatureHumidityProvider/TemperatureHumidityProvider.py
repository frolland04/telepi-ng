# -*- coding: UTF-8 -*-

# Dépendances
import threading
import time

# Sous-modules
import Debug

fileName = __file__.split('\\')[-1]


class TemperatureHumidityProvider:
    TIMER_PERIOD_SECS = 20

    @Debug.call_log
    def __init__(self, ex):
        # Handle pour exécuter les requêtes à la BDD
        self.ex = ex

        # Dernières mesures
        self.__humidity = 0
        self.__temperature = 0

        # Timer de déclenchement des mesures et condition d'arrêt
        self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
        self.end = False
        self.t.start()

    @Debug.call_log
    def close(self):
        """Fin propre : arrêt timer si en attente et pas de relance si en cours d'exécution grâce à condition d'arrêt"""
        self.end = True
        self.t.cancel()

    @Debug.call_log
    def run(self):
        print("** Mesure de l'environnement **")
        self.__humidity += 1
        self.__temperature += 1.1

        if not self.end:
            # On relance pour une prochaine occurrence
            self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
            self.t.start()

    @property
    def humidity(self):
        """I'm the 'humidity' property."""
        print("humidity.get")
        return self.__humidity

    @property
    def temperature(self):
        """I'm the 'temperature' property."""
        print("temperature.get")
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
