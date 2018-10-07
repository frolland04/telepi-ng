# -*- coding: UTF-8 -*-

# Dépendances
import threading

# *** On importe le pilote LCD (lcd_lib + i2c_lib) ***
# Nécessite 'python3-smbus' : se promener dans le dossier 'io'
import lcd_lib

# Sous-modules
import Debug  # Besoin de mon décorateur 'call_log'


file = __file__.split('\\')[-1]


class RunningLcdOutput:
    """
    Une classe pour gérer un écran LCD sur bus I2C, 2 lignes de 16 caractères.
    Affichage tournant d'une liste d'informations.
    """

    TIMER_PERIOD_SECS = 5

    @Debug.call_log
    def __init__(self):
        # On initialise le LCD, selon le montage télépi
        # LCD 16X02 & PCF8574T I2C @=0x27 (5V)
        self.lcd = lcd_lib.lcd()

        # On efface l'écran
        self.lcd.lcd_clear()

        # Préparation du timer et condition d'arrêt
        self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
        self.end = False
        self.t.start()

        # Les éléments à afficher
        self.__items = {'Initialisation': '...', 'Patientez': '...'}

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

        # On copie notre dictionnaire pour travailler sur un contenu stable
        # (Il pourrait être modifié pendant ce temps)
        items_dict = dict(self.__items)

        # On fabrique une liste des clés
        items_list = list(items_dict)

        if not len(items_list) == 0:
            # On s'assure que l'index n'a pas dépassé l'actuelle capacité
            # Sinon on rembobine
            if self.itemIndex >= len(items_list):
                self.itemIndex = 0

            # On récupère les données à afficher
            item_ligne1 = items_list[self.itemIndex]
            item_ligne2 = items_dict[item_ligne1]

            # Affiche l'item à l'index 'self.itemIndex' => la clé et son contenu
            print('DBG:', self.itemIndex, items_dict, items_list, "->", item_ligne1, item_ligne2)
            
            # On efface l'écran
            self.lcd.lcd_clear()

            # On affiche des caractères sur chaque ligne
            # Sur la ligne 1, la clé, et sur la ligne 2 l'élément associé
            self.lcd.lcd_display_string(item_ligne1, 1)
            self.lcd.lcd_display_string(item_ligne2, 2)

            # On programme l'item suivant pour le tour suivant
            self.itemIndex += 1
        else:
            print(file + ":", 'La liste des éléments à afficher est vide.')
            self.itemIndex = 0

        if not self.end:
            # On relance pour une prochaine occurrence
            self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
            self.t.start()

    @property
    def items(self):
        """Je suis une @propriété Python."""
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
