# -*- coding: UTF-8 -*-

# Dépendances
import threading
import time

# Sous-modules
import Debug  # Besoin de mon décorateur 'call_log'

file = __file__.split('\\')[-1]


class RunningLcdOutput:
    TIMER_PERIOD_SECS = 3

    @Debug.call_log
    def __init__(self):
        # Préparation du timer et condition d'arrêt
        self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
        self.end = False
        self.t.start()

        # Les éléments à afficher
        self.__items = {'Démarrage': '...', 'Patientez': '...'}

        # Affiche l'item 0 au démarrage
        self.itemIndex = 0

    @Debug.call_log
    def close(self):
        """Fin propre : arrêt timer si en attente et pas de relance si en cours d'exécution grâce à condition d'arrêt"""
        self.end = True
        self.t.cancel()

    @Debug.call_log
    def run(self):
        print("** Affichage **")

        if not len(self.__items) == 0:
            try:
                # A condition que la liste ne soit pas vide, on en affiche son contenu
                # Affiche l'item à l'index 'self.item'
                item = list(self.__items)[self.itemIndex]
                print(item, self.__items[item])

                # On programme l'item suivant pour le tour suivant
                self.itemIndex += 1
                if self.itemIndex >= len(self.__items):
                    self.itemIndex = 0
            except:
                print(file + ":", "Ooops, il est difficile d'accéder à la liste des éléments à afficher!")
                self.itemIndex = 0
        else:
            print(file + ":", 'La liste des éléments à afficher est vide.')
            self.itemIndex = 0

        if not self.end:
            # On relance pour une prochaine occurrence
            self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
            self.t.start()

    @property
    def items(self):
        """I'm the 'items' property."""
        print("RunningLcdOutput.items@get")
        return self.__items

    @items.setter
    def items(self, val):
        print("RunningLcdOutput.items@set")
        self.__items = val

    @Debug.call_log
    def __enter__(self):
        print('...')

    @Debug.call_log
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @Debug.call_log
    def __del__(self):
        print('...')
