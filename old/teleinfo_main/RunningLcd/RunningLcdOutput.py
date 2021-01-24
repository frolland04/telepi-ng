#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


# Dépendances
import threading
import time

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
    print('[DBG]', *args)
    

class RunningLcdOutput:
    """
    Une classe pour gérer un écran LCD sur bus I2C, 2 lignes de 16 caractères ou 4 lignes de 20 caractères.
    Affichage tournant d'une liste d'informations, composée de plusieurs pages.
    """

    # Durée d'affichage d'une page
    TIMER_PERIOD_SECS = 4

    # Nombre de lignes maximum sur LCD
    LCD_LINES = 4

    # Longueur maximum d'une ligne en caractères
    LCD_LINE_WIDTH = 20

    @Debug.log_class_func
    def __init__(self):
        """
        Initialisation du 'RunningLcdOutput' : bibliothèque LCD/I2C, timer et données
        """
        # On initialise le LCD, selon le montage télépi
        # LCD 16X02,20X04 & PCF8574T I2C @=0x27 (5V)
        self.lcd = lcd_lib.lcd()

        # On efface l'écran
        self.lcd.lcd_clear()

        # Préparation du timer et de la condition d'arrêt
        self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
        self.end = False
        self.t.start()

        # Les éléments à afficher, par page, dans chaque page, par ligne
        # xxxxxxxxxx = '12345678901234567890'
        self.pages = [['** Initialisation **', '...', '12345678901234567890', '...'],
                      ['** Patientez, svp **', '...', '12345678901234567890', '...']]

        # Affiche la page 0 au démarrage
        self.page_index = 0

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

        # On copie notre liste de pages pour travailler sur un contenu stable
        # (Il pourrait être modifié pendant ce temps)
        page_list = list(self.pages)

        if not len(page_list) == 0:
            # On s'assure que l'index n'a pas dépassé l'actuelle capacité
            # Sinon on rembobine, retour à la première page!
            if self.page_index >= len(page_list):
                self.page_index = 0

            # On récupère les données à afficher, pour la page courante
            current_page = page_list[self.page_index]

            # Affiche l'item à l'index 'self.itemIndex' => la clé et son contenu
            dbg_msg('MESSAGES_LCD:', self.page_index, current_page)

            # On efface l'écran
            self.lcd.lcd_clear()

            # On affiche des caractères sur chaque ligne du LCD
            for line_index in range(self.LCD_LINES):
                information = ''

                # Si une ligne est indiquée pour cette page, on récupère le contenu
                # sinon elle restera vide
                if line_index < len(current_page):
                    information = '{: ^20}'.format(current_page[line_index])  # centré dans une zone de 20 espaces

                # Si on est sur la dernière ligne du LCD, on ajoute l'indicateur d'avancement
                if line_index == self.LCD_LINES - 1:
                    footer = str(self.page_index + 1) + '/' + str(len(page_list))
                    information = footer + information[len(footer):]

                dbg_msg(line_index, ':', information)
                self.lcd.lcd_display_string(information, line_index+1)

            # On programme la page suivante pour le tour suivant
            self.page_index += 1
        else:
            dbg_msg(this_file + ":", 'La liste des éléments à afficher est vide.')
            self.page_index = 0

        if not self.end:
            # On relance pour une prochaine occurrence
            self.t = threading.Timer(self.TIMER_PERIOD_SECS, self.run)
            self.t.start()

    @Debug.log_class_func
    def set_message(self, page_index, line_index, message_string):
        """
        Permet de manipuler le message sur une ligne d'une page, ajoute des pages si nécessaire.
        """
        dbg_msg('page', page_index, 'line', line_index, 'message', message_string)
        page = ['..', '..', '..', '..']

        # Si pas déjà assez de pages, on les rajoute
        if not page_index < len(self.pages):
            dbg_msg('La liste doit être étendue!')
            while page_index > len(self.pages)-1:
                self.pages.append(list(page))

        # Maintenant on accède à la page demandée et on modifie la ligne souhaitée
        page = self.pages[page_index]

        if line_index in range(self.LCD_LINES):
            page[line_index] = message_string

    # @Debug.log_class_func
    def set_page(self, page_index, lines):
        """
        Permet de manipuler les lignes d'une page en une seule opération.
        """
        dbg_msg('page', page_index, 'lines', lines)
        for line_index in range(len(lines)):
            self.set_message(page_index, line_index, lines[line_index])

    @Debug.log_class_func
    def clear(self):
        """
        Permet de supprimer toutes les pages existantes.
        """
        self.pages.clear()
        self.pages.append(['..', '..', '..', '..'])

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


if __name__ == "__main__":
    """
    Un petit bout de programme de test, pour voir ce que cela donne
    """
    print("test begin!")

    try:
        lcd = RunningLcdOutput()
        lcd.set_message(0, 0, 'oui')
        lcd.set_message(1, 0, 'non')
        lcd.set_message(2, 0, 'ne sait pas')
        lcd.set_message(9, 0, 'waouh')
        time.sleep(45)  # 45s
        lcd.clear()
        lcd.set_message(0, 0, 'non non non')
        lcd.set_page(3, ('quand même', 'ici', 'pas comme', 'ailleurs'))
        time.sleep(3600)  # one hour

    except (Exception, KeyboardInterrupt, SystemExit) as e:
        lcd.close()
        raise e

    print("test end.")
