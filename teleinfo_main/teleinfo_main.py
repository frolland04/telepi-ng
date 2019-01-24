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

# Quelques informations
__author__ = 'Frédéric ROLLAND'
__version__ = '1'


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
print("Version:", sys.version_info)
print("PATH:", sys.path)
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
disp_dict = lcd.items
disp_dict.clear()

# Récupère l'accès aux valeurs remontées par la collecte ERDF
edis_tags = ti.tags

stop = False
while not stop:
    try:
        print('>>> go')

        # ---------------------------------------------------------------
        # Récupérer les données et les transmettre là où c'est nécessaire
        # ---------------------------------------------------------------

        # Depuis l'horloge système : la date et l'heure
        sys_clock = datetime.datetime.now()

        # Depuis TemperatureHumidityProvider : température, humidité relative et pression atmosphérique
        env_temp = thp.temperature
        env_hum = thp.humidity
        env_atm = thp.pressure

        # Depuis MessageProcessor :
        # barème ERDF en cours, intensité instantanée, puissance apparente et validité mesure
        edis_dict = dict(edis_tags)
        edis_bareme = edis_dict['PTEC']
        edis_puissance = int(edis_dict['PAPP'])
        edis_intensite = int(edis_dict['IINST'])
        edis_ok = edis_dict['OK']

        # Depuis la BDD pour quelques informations
        # notamment des compteurs sur l'activité et l'empreinte mémoire de la BDD
        db_rows = dex.pool.getDatabaseHistoRowNb()
        db_heapmax = dex.pool.getDatabaseGlobalHeapMax()
        db_tbspace = dex.pool.getDatabaseHistoTablespace()
        db_recvmsgs = dex.pool.getCountRecvMsgOk()

        # -------------------------------------
        # Envoyer les données à l'affichage LCD
        # -------------------------------------

        # Remontée des données Téléinformation
        if edis_ok:
            disp_dict['TARIF:'] = '  ' + edis_bareme
            disp_dict['IINST(A),PAPP(W)'] = '{:05d}  {:05d}'.format(edis_intensite, edis_puissance)
        else:
            disp_dict['TARIF:'] = '  ' + '???'
            disp_dict['IINST(A),PAPP(W)'] = '?????  ?????'

        # Remontée des données d'environnement
        disp_dict['TEMP.(C),HUM.(%)'] = '{:05.1f}  {:05.1f}'.format(env_temp, env_hum)
        disp_dict['PRESSION ATMOS.'] = '{:06.2f} (hPa)'.format(env_atm)

        # Divers éléments
        disp_dict['HORLOGE:'] = sys_clock.strftime('%d/%m/%Y %H:%M')

        # Statistiques et données remontées par la BDD
        disp_dict['TELEINFO:'] = '{:010d} MESS.'.format(db_recvmsgs)
        disp_dict['HISTO:'] = '{:010d} MESS.'.format(db_rows)
        disp_dict['MEM. / MAX.(MB):'] = '{:06.2f} / {:06.2f}'.format(db_tbspace, db_heapmax)

        # ------------------------------------------
        # Envoyer les données pour stockage à la BDD
        # ------------------------------------------

        if edis_ok:
            # On ajoute la température et l'humidité relevées périodiquement
            # aux valeurs du dictionnaire issu de la collecte, pour l'historique en BDD
            edis_dict['TEMPERATURE'] = env_temp
            edis_dict['RH'] = env_hum
            edis_dict['PRESSION_ATMOS'] = env_atm

            # Historique des valeurs échantillonnées toutes les 20s
            dex.pool.updateTeleinfoHisto(edis_dict)

        # On se reverra dans 30s
        time.sleep(30)

    except Exception as e:
        # Affiche le problème
        print('\n>>> ERREUR :\n', e, '\n')

        # En cas de souci, on quitte la boucle
        print(">>> INTERRUPTED !")
        dex.pool.notifySystemFatalCondition()
        stop = True

# Message final sur l'écran LCD
disp_dict.clear()
disp_dict['STOP'] = 'PROGRAMME'

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
