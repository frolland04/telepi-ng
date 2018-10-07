#!/usr/bin/python
# -*- coding: UTF-8 -*-


# *** Dépendances ***
import sys
import time
import datetime

# *** Sous-modules ***
import DatabaseEngine
import TeleInfo
import TemperatureHumidityProvider
import RunningLcd
import StatusLeds


# ================================================================================
# NAME: TELEINFO
# AUTHORS: Frédéric ROLLAND, depuis une idée et un code original de Sébastien Joly
# DATE : 2017-12-23
# COMMENT: Collecteur de trames Télé-Information ERDF et des caractéristiques
# de l'environnement proche (température et humidité relative).
# Historisation en BDD et affichage tournant sur LCD.
# ================================================================================


file = __file__.split('/')[-1]


def etat_presence_programme(si):
    """LED bleue"""
    try:
        si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_B)
    except:
        return

def etat_sortie_programme(si):
    """LED rouge, seule"""
    try:
        si.set_off()
        si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_R)
    except:
        return

def etat_echec_demarrage(si):
    """LED rouge et LED jaune"""
    try:
        si.set_off()
        si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_R)
        si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_Y)
    except:
        return

def etat_programme_actif(si):
    """LED verte"""
    try:
        si.set_on(StatusLeds.GpioLedController.GPIO_ID_LED_G)
    except:
        return


print("File:", file)
print("Runtime:", sys.version)
print("**** Bonjour tout le monde ! ****")


# =============================
# *** Programme principal ! ***
# =============================


# Afficheur 4 LEDs : chenillard puis LED bleue allumée
# ----------------------------------------------------
leds = StatusLeds.GpioLedController()
leds.running_leds()
etat_presence_programme(leds)


# Démarrage de l'écran LCD
# ------------------------

try:
    lcd = RunningLcd.RunningLcdOutput()
except:
    print("Affichage LCD indisponible!")
    etat_echec_demarrage(leds)
    sys.exit(-1)

# Tentative de connexion à la base de données
# -------------------------------------------

try:
    dex = DatabaseEngine.SafeRequestExecutor()
except:
    print("Base de données indisponible!")
    lcd.items = {'ERREUR': 'Acces BDD', 'Initialisation': 'impossible'}
    etat_echec_demarrage(leds)
    sys.exit(-2)

# Tentative de connexion au port série
# ------------------------------------

try:
    ti = TeleInfo.MessageProcessor(dex)
except:
    print("Entrée série indisponible!")
    lcd.items = {'ERREUR': 'Acces Teleinfo', 'Initialisation': 'impossible'}
    etat_echec_demarrage(leds)
    sys.exit(-3)

# Température et humidité relative relevées périodiquement
# --------------------------------------------------------

try:
    thp = TemperatureHumidityProvider.TemperatureHumidityProvider(dex)
except:
    print("Mesure de l'environnement indisponible!")
    lcd.items = {'ERREUR': 'Acces TEMP/HUM', 'Initialisation': 'impossible'}
    etat_echec_demarrage(leds)
    sys.exit(-4)

# Boucle de réception des messages
# --------------------------------

# La LED verte indique que tout a bien démarré
etat_programme_actif(leds)

# Attente du démarrage de tous les composants
# et de l'approvisionnement des premières valeurs
time.sleep(30)

# Récupère l'accès au contenu affiché sur le LCD
# et efface l'écran
disp = lcd.items
disp.clear()

# Récupère l'accès aux valeurs remontées par la collecte ERDF
tags = ti.tags

stop = False
while not stop:
    try:
        print('>>> go')
        print('DBG_MAIN:', tags)

        # ---------------------------------------------------------------
        # Récupérer les données et les transmettre là où c'est nécessaire
        # ---------------------------------------------------------------

        # Depuis l'horloge système : la date et l'heure
        sysclock = datetime.datetime.now()

        # Depuis TemperatureHumidityProvider : température et humidité relative
        temp = round(thp.temperature, 1)
        hum = round(thp.humidity, 1)

        # Depuis MessageProcessor :
        # barème ERDF en cours, intensité instantanée, puissance apparente et validité mesure
        bareme = tags['PTEC']
        puissance = int(tags['PAPP'])
        intensite = int(tags['IINST'])
        collecte_ok = tags['OK']

        # -----------------------
        # Appliquer à l'affichage
        # -----------------------

        if collecte_ok:
            disp['TARIF'] = bareme
            disp['IINST(A),PAPP(W)'] = '{:7.1f}'.format(intensite) + ' ' + '{:7.1f}'.format(puissance)
        else:
            disp['TARIF'] = '???'
            disp['IINST(A),PAPP(W)'] = '    ???     ???'

        disp['TEMP(C), HUM(%)'] = '{:7.1f}'.format(temp) + ' ' + '{:7.1f}'.format(hum)
        disp['HORLOGE'] = sysclock.strftime('%d/%m/%Y %H:%M:%S')

        # ------------------------------
        # Appliquer à la base de données
        # ------------------------------

        if collecte_ok:
            # On ajoute la température et l'humidité relevées périodiquement
            # aux valeurs du dictionnaire issu de la collecte
            tags['TEMPERATURE'] = temp
            tags['RH'] = hum

            # Jeu unique de valeurs instantanées
            dex.pool.updateTeleinfoInst(tags)

            # Historique de toutes les valeurs
            dex.pool.updateTeleinfoHisto(tags)

        # On se revoit dans 10s
        time.sleep(10)

    except Exception as e:
        # Affiche le problème
        print('ERREUR', e)

        # En cas de souci, on quitte la boucle
        print(">>> INTERRUPTED !")
        dex.pool.notifySystemFatalCondition()
        stop = True

# Message final sur l'écran LCD
disp.clear()
disp['STOP'] = 'Fin du programme' 

# LED rouge allumée, toute seule
etat_sortie_programme(leds)

# Arrêt de la collecte Téléinfo ERDF
ti.close()

# Arrêt des mesures de l'environnement
thp.close()

# Libération de l'écran LCD
lcd.close()

# Libération de la BDD
dex.close()

# On s'en va maintenant
sys.exit(-5)
