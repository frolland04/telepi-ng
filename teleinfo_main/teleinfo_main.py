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
import Debug  # Besoin de mon décorateur "log_class_func" & "EnterExitLogger"


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

# Pour le débogage
this_file = __file__.split('\\')[-1]

print("File:", this_file)
print("Runtime:", sys.version)
print("Version:", sys.version_info)
print("PATH:", sys.path)
print("**** Bonjour tout le monde ! ****")

# =============================
# *** Programme principal ! ***
# =============================

# Les codes de retour en cas de problème
SYSEXIT_ERROR_LEDS = -1
SYSEXIT_ERROR_LCD = -2
SYSEXIT_ERROR_DBE = -3
SYSEXIT_ERROR_MPR = -4
SYSEXIT_ERROR_THP = -5
SYSEXIT_ERROR_PRE = -6
SYSEXIT_ERROR_INT = -7

# Afficheur 5 LEDs : chenillard puis LED bleue allumée
# ----------------------------------------------------

try:
    leds = StatusLeds.GpioLedController()
    leds.running_leds()
    StatusLeds.SystemLeds.presence(leds)

except (BaseException, KeyboardInterrupt, SystemExit) as e:
    print("Afficheur 5 LED indisponible!", e)
    sys.exit(SYSEXIT_ERROR_LEDS)

# Démarrage de l'écran LCD
# ------------------------

try:
    lcd = RunningLcd.RunningLcdOutput()

except (BaseException, KeyboardInterrupt, SystemExit) as e:
    print("Affichage LCD indisponible!", e)
    StatusLeds.SystemLeds.initialization_failed(leds)
    sys.exit(SYSEXIT_ERROR_LCD)

# Tentative de connexion à la base de données
# -------------------------------------------

try:
    dex = DatabaseEngine.SafeRequestExecutor()

except (BaseException, KeyboardInterrupt, SystemExit) as e:
    print("Base de données indisponible!", e)
    lcd.items = {'ERREUR': 'BDD', 'Initialisation': 'impossible'}
    StatusLeds.SystemLeds.initialization_failed(leds)
    sys.exit(SYSEXIT_ERROR_DBE)

# Tentative de connexion au port série
# ------------------------------------

try:
    ti = TeleInfo.MessageProcessor(dex)

except (BaseException, KeyboardInterrupt, SystemExit) as e:
    print("Entrée série indisponible!", e)
    lcd.items = {'ERREUR': 'TELEINFO', 'Initialisation': 'impossible'}
    StatusLeds.SystemLeds.initialization_failed(leds)
    sys.exit(SYSEXIT_ERROR_MPR)

# Température et humidité relative relevées périodiquement
# --------------------------------------------------------

try:
    thp = TemperatureHumidityProvider.TemperatureHumidityProvider(dex)

except (BaseException, KeyboardInterrupt, SystemExit) as e:
    print("Mesure de l'environnement indisponible!", e)
    lcd.items = {'ERREUR': 'BME280', 'Initialisation': 'impossible'}
    StatusLeds.SystemLeds.initialization_failed(leds)
    sys.exit(SYSEXIT_ERROR_THP)

# Préparation de la boucle principale
# -----------------------------------

try:
    # La LED verte indique que tout a bien démarré
    StatusLeds.SystemLeds.initialized(leds)

    # On complète par un flash sur la LED blanche :-)
    StatusLeds.SystemLeds.running(leds)

    # Attente du démarrage de tous les composants
    # et de l'approvisionnement des premières valeurs
    time.sleep(30)

    # Récupère l'accès au contenu affiché sur le LCD
    # et efface l'écran
    disp = lcd.items
    disp.clear()

    # Récupère l'accès aux valeurs remontées par la collecte ERDF
    tags = ti.tags

except (BaseException, KeyboardInterrupt, SystemExit) as e:
    print("Erreur pendant la préparation de la boucle principale!", e)
    lcd.items = {'ERREUR': 'PREPARATION', 'Initialisation': 'impossible'}
    StatusLeds.SystemLeds.initialization_failed(leds)
    sys.exit(SYSEXIT_ERROR_PRE)

# --------------------------------------------- DEBUT BOUCLE PRINCIPALE ---------------------------------------------
stop = False
while not stop:
    try:
        print('>>> GO!')

        # Encore un flash sur la LED blanche :-) à chaque tour!
        StatusLeds.SystemLeds.running(leds)

        # ---------------------------------------------------------------
        # Récupérer les données et les transmettre là où c'est nécessaire
        # ---------------------------------------------------------------

        # Depuis l'horloge système : la date et l'heure
        sys_clock = datetime.datetime.now()

        # Depuis 'TemperatureHumidityProvider' : température, humidité relative et pression atmosphérique
        env_temp = thp.temperature
        env_hum = thp.humidity
        env_atm = thp.pressure

        # Depuis 'MessageProcessor' :
        # barème ERDF en cours, intensité instantanée, puissance apparente et validité mesure
        # (on recopie le message de téléinformation courant)
        mesure = dict(tags)
        edis_bareme = mesure['PTEC']
        edis_puissance = int(mesure['PAPP'])
        edis_intensite = int(mesure['IINST'])
        edis_ok = mesure['OK']

        # Depuis la BDD pour quelques informations
        # notamment des compteurs sur l'activité et l'empreinte mémoire de la BDD
        db_rows = dex.pool.getDatabaseHistoRowNb()
        db_heapmax = dex.pool.getDatabaseGlobalHeapMax()
        db_tbspace = dex.pool.getDatabaseHistoTablespace()
        db_recvmsgs = dex.pool.getCountRecvMsgOk()

        # -------------------------------------
        # Envoyer les données à l'affichage LCD
        # -------------------------------------

        # Affichage des données de Téléinformation
        if edis_ok:
            disp['TARIF:'] = '  ' + edis_bareme
            disp['IINST(A),PAPP(W)'] = '{:05d}  {:05d}'.format(edis_intensite, edis_puissance)
        else:
            disp['TARIF:'] = '  ' + '???'
            disp['IINST(A),PAPP(W)'] = '?????  ?????'

        # Affichage des données d'environnement
        disp['TEMP.(C),HUM.(%)'] = '{:05.1f}  {:05.1f}'.format(env_temp, env_hum)
        disp['PRESSION ATMOS.'] = '{:06.2f} (hPa)'.format(env_atm)

        # Affichage de divers éléments
        disp['HORLOGE:'] = sys_clock.strftime('%d/%m/%Y %H:%M')

        # Affichage des statistiques et des données remontées par la BDD
        disp['TELEINFO:'] = '{:010d} MESS.'.format(db_recvmsgs)
        disp['HISTO:'] = '{:010d} MESS.'.format(db_rows)
        disp['MEM. / MAX.(MB):'] = '{:06.2f} / {:06.2f}'.format(db_tbspace, db_heapmax)

        # ------------------------------------------
        # Envoyer les données pour stockage à la BDD
        # ------------------------------------------

        if edis_ok:
            # On ajoute la température et l'humidité relevées périodiquement
            # aux valeurs du dictionnaire issu de la collecte, pour l'historique en BDD
            mesure['TEMPERATURE'] = env_temp
            mesure['RH'] = env_hum
            mesure['PRESSION_ATMOS'] = env_atm

            # Historique des valeurs échantillonnées toutes les 20s
            dex.pool.updateTeleinfoHisto(mesure)

        # ------------------------------
        # On se reverra dans 30 secondes
        # ------------------------------
        time.sleep(30)

    # En cas de souci, on quitte directement la boucle avant le prochain tour!
    # ------------------------------------------------------------------------
    except (BaseException, KeyboardInterrupt, SystemExit) as e:
        print('>>> INTERRUPTED !', e)
        dex.pool.notifySystemFatalCondition()
        stop = True

    print('STOP?', stop)
# -------------------------------------------- FIN DE LA BOUCLE PRINCIPALE --------------------------------------------

# C'est la séquence de fin!
print('STOP!')

# Message final sur l'écran LCD
disp.clear()
disp['STOP'] = 'PROGRAMME'
print('[Final status on display.]')

# LED rouge allumée, toute seule
StatusLeds.SystemLeds.aborted(leds)
print('[Final status on leds.]')

# Arrêt de la collecte Téléinfo ERDF
ti.close()
print('[Data collection released.]')

# Arrêt des mesures de l'environnement
thp.close()
print('[Monitoring released.]')

# Libération de l'écran LCD
lcd.close()
print('[Display released.]')

# Libération de la BDD
dex.close()
print('[Database closed.]')

# On s'en va maintenant, on sort réellement si tous les autres threads sont terminés
sys.exit(SYSEXIT_ERROR_INT)
print('SHOULD NOT BE HERE.')
