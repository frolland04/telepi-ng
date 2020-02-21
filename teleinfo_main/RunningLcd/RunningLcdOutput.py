# -*- coding: UTF-8 -*-


# Dépendances
import threading

# *** On importe le pilote LCD (lcd_lib + i2c_lib) ***
# Nécessite 'python3-smbus' : se promener dans le dossier 'io'
import lcd_lib

# Sous-modules
import Debug  # Besoin de mon décorateur "log_class_func" & "EnterExitLogger"

# Pour le débogage
this_file = __file__.split('\\')[-1]


def dbg_msg(*args):
    """
    Hook to print (or not) debugging messages for this Python file.
    """
    # print('[DBG]', *args) # -- disabled!
    

class RunningLcdOutput:
    """
    Une classe pour gérer un écran LCD sur bus I2C, 2 lignes de 16 caractères.
    Affichage tournant d'une liste d'informations.
    """

    TIMER_PERIOD_SECS = 4

    @Debug.log_class_func
    def __init__(self):
        """
        Initialisation du 'RunningLcdOutput' : bibliothèque LCD/I2C, timer et données
        """
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
        # xxxxxxxxxxx = '12345678901234567890'
        self.__items = {'** Initialisation **': '...',
                        '** Patientez, svp **': '...'}

        # Affiche l'item 0 au démarrage
        self.itemIndex = 0

        # On veut déboguer les entrées/sorties de contexte d'exécution
        self.ct = Debug.EnterExitLogger('RunningLcdOutput')

    @Debug.log_class_func
    def __del__(self):
        """
        Nettoyage du 'RunningLcdOutput'
        """
        print('...')

    @Debug.log_class_func
    def close(self):
        """
        Fin propre du 'RunningLcdOutput' : arrêt timer si en attente et pas de relance si en cours d'exécution,
        grâce à condition d'arrêt
        """
        # On signale l'arrêt
        self.end = True

        # On annule le timer
        # self.t.cancel() @todo: faire une fin propre qui annule le timer et affiche le message de fin.

    @Debug.log_class_func
    def run(self):
        """
        Corps du timer : traitement exécuté périodiquement
        """
        dbg_msg("** Affichage **")

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
            header      = items_list[self.itemIndex]
            information = items_dict[header]
            information = '{: ^20}'.format(information)  # centré dans une zone 20 espaces
            footer      = str(self.itemIndex + 1) + ' / ' + str(len(items_list))

            # Affiche l'item à l'index 'self.itemIndex' => la clé et son contenu
            dbg_msg('MESSAGES_LCD:', self.itemIndex, items_dict, items_list, "->", header, information, footer)

            # On efface l'écran
            self.lcd.lcd_clear()

            # On affiche des caractères sur chaque ligne
            # Sur la ligne 1, la clé, et sur la ligne 2 l'élément associé. La ligne 3 reste vide et la 4
            # servira d'indice de progression.
            self.lcd.lcd_display_string(header, 1)
            self.lcd.lcd_display_string(information, 2)
            self.lcd.lcd_display_string(footer, 4)

            # On programme l'item suivant pour le tour suivant
            self.itemIndex += 1
        else:
            dbg_msg(this_file + ":", 'La liste des éléments à afficher est vide.')
            self.itemIndex = 0

        if not self.end:
            # On relance pour une prochaine occurrence
            self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
            self.t.start()

    @property
    def items(self):
        """
        Je suis une @propriété Python en lecture.
        """
        print("@RunningLcdOutput.items")
        return self.__items

    @items.setter
    def items(self, val):
        """
        Je suis une @propriété Python en écriture.
        """
        print("RunningLcdOutput.items=")
        self.__items = val

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
        self.close()
        return self.ct.__exit__(exc_type, exc_val, exc_tb)
