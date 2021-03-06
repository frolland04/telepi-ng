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
import SystemInfoProvider
import Debug  # Besoin de mon décorateur "log_class_func" & "EnterExitLogger"


# ================================================================================
# NAME: TELEINFO
# AUTHORS: Frédéric ROLLAND, depuis une idée et un code original de Sébastien Joly
# DATE : 2017-12-23
# COMMENT: Collecteur de trames Télé-Information ERDF et des caractéristiques
# de l'environnement proche (température et humidité relative).
# Historisation en BDD et affichage tournant sur LCD, ainsi que bargraph et leds
# pour indiquer l'état du programme.
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
SYSEXIT_ERROR_LCD  = -2
SYSEXIT_ERROR_DBE  = -3
SYSEXIT_ERROR_MPR  = -4
SYSEXIT_ERROR_THP  = -5
SYSEXIT_ERROR_PRE  = -6
SYSEXIT_ERROR_INT  = -7
SYSEXIT_ERROR_TEST = -8


# Le nom du service de l'application
TELEINFO_SERVICE_UNIT_NAME = 'teleinfo.service'

# Les messages d'erreur tournants sur le LCD
LCD_PAGE_ERROR_TEST     = ('ERREUR', 'TEST',        'Initialisation', 'impossible')
LCD_PAGE_ERROR_DATABASE = ('ERREUR', 'BDD',         'Initialisation', 'impossible')
LCD_PAGE_ERROR_TELEINFO = ('ERREUR', 'TELEINFO',    'Initialisation', 'impossible')
LCD_PAGE_ERROR_BME280   = ('ERREUR', 'BME280',      'Initialisation', 'impossible')
LCD_PAGE_ERROR_PREP     = ('ERREUR', 'PREPARATION', 'Initialisation', 'impossible')

# Les bannières des messages envoyés au LCD
LCD_MSG_HDR_TAR  = '*****  TARIF   *****'
LCD_MSG_HDR_IIPA = '* IINST(A),PAPP(W) *'
LCD_MSG_HDR_TH   = '* TEMP.(C),HUM.(%) *'
LCD_MSG_HDR_PATM = '* PRESSION ATMOSP. *'
LCD_MSG_HDR_HOR  = '****  HORLOGE   ****'
LCD_MSG_HDR_REST = '***  RESTART NB  ***'
LCD_MSG_HDR_SVUP = '** SERVICE UPTIME **'
LCD_MSG_HDR_SSUP = '** SYSTEM UPTIME  **'
LCD_MSG_HDR_TEL  = '*DECODAGE TELEINFOR*'
LCD_MSG_HDR_HIST = '**** HISTORIQUE ****'
LCD_MSG_HDR_DBTB = '***** MEM.(MB) *****'
LCD_MSG_HDR_DBHP = '***** MAX.(MB) *****'
# xxxxxxxxxxxxxx = '12345678901234567890'

try:
    # ---------------------------------------------
    # Séquence principale :
    # - initialisation,
    # - préparation,
    # - boucle principale
    # Si exception inattendue : bloc de terminaison
    # ---------------------------------------------

    # ------------------- Initialisation ------------------
    # Afficheur 5 LEDs : chenillards puis LED bleue allumée
    # -----------------------------------------------------

    try:
        leds = StatusLeds.GpioLedController()

        StatusLeds.SystemLeds.running_leds(leds)
        StatusLeds.SystemLeds.presence(leds)
        StatusLeds.BargraphLeds.running_leds(leds)

    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print("[Affichage LED indisponible! Abandon.]", e)
        sys.exit(SYSEXIT_ERROR_LEDS)

    else:
        print("[Affichage LED OK.]")

    # ------------------- Initialisation --------------------
    # Démarrage de la gestion de l'écran LCD, connecté en I2C
    # -------------------------------------------------------

    try:
        lcd = RunningLcd.RunningLcdOutput()

    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print("[Affichage LCD indisponible! Abandon.]", e)
        StatusLeds.SystemLeds.initialization_failed(leds)
        sys.exit(SYSEXIT_ERROR_LCD)

    else:
        print("[Affichage LCD OK.]")

    # ------------------ Initialisation -------------------
    # Provoque un échec volontaire (uniquement pour tester)
    # -----------------------------------------------------

    try:
        # raise Exception  # à commenter pour éviter l'échec!
        print('(...)')

    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print("Echec volontaire! Abandon.", e)
        lcd.clear()
        lcd.set_page(0, LCD_PAGE_ERROR_TEST)
        StatusLeds.SystemLeds.initialization_failed(leds)
        sys.exit(SYSEXIT_ERROR_TEST)

    else:
        print("[Test d'échec volontaire non utilisé pour cette fois.]")

    # ------------------ Initialisation -----------------
    # Tentative de connexion à la base de données MariaDB
    # ---------------------------------------------------

    try:
        dex = DatabaseEngine.SafeRequestExecutor()

    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print("Base de données indisponible! Abandon.", e)
        lcd.clear()
        lcd.set_page(0, LCD_PAGE_ERROR_DATABASE)
        StatusLeds.SystemLeds.initialization_failed(leds)
        sys.exit(SYSEXIT_ERROR_DBE)

    else:
        print("[Connexion BDD OK.]")

    # ----------------------- Initialisation ----------------------
    # Tentative de connexion au port série / entrée Téléinfo ENEDIS
    # -------------------------------------------------------------

    try:
        ti = TeleInfo.MessageProcessor(dex)

    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print("Connexion TELEINFO indisponible! Abandon.", e)
        lcd.clear()
        lcd.set_page(0, LCD_PAGE_ERROR_TELEINFO)
        StatusLeds.SystemLeds.initialization_failed(leds)
        sys.exit(SYSEXIT_ERROR_MPR)

    else:
        print("[Connexion TELEINFO OK.]")

    # --------------------- Initialisation -------------------
    # Température et humidité relative relevées périodiquement
    # --------------------------------------------------------

    try:
        thp = TemperatureHumidityProvider.TemperatureHumidityProvider(dex)

    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print("Connexion BME280 indisponible! Abandon.", e)
        lcd.clear()
        lcd.set_page(0, LCD_PAGE_ERROR_BME280)
        StatusLeds.SystemLeds.initialization_failed(leds)
        sys.exit(SYSEXIT_ERROR_THP)

    else:
        print("[Connexion BME280 OK.]")

    # -------------------------- Préparation ---------------------------
    # Temporisation d'attente avant le passage dans la boucle principale
    # ------------------------------------------------------------------

    try:
        # La LED verte indique que tout a bien démarré
        StatusLeds.SystemLeds.initialized(leds)

        # On complète par un flash sur la LED blanche :-)
        StatusLeds.SystemLeds.running(leds)

        # Attente du démarrage de tous les composants
        # et de l'approvisionnement des premières valeurs
        time.sleep(30)

        # On efface l'écran
        lcd.clear()

        # Récupère une référence aux valeurs remontées par la collecte ERDF
        tags = ti.tags

    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print("Erreur pendant la préparation de la boucle principale!", e)
        lcd.clear()
        lcd.set_page(0, LCD_PAGE_ERROR_PREP)
        StatusLeds.SystemLeds.initialization_failed(leds)
        sys.exit(SYSEXIT_ERROR_PRE)

    # -------------------------------------------- DEBUT BOUCLE PRINCIPALE ---------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
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

            # Depuis la BDD pour quelques informations :
            # notamment des compteurs sur l'activité et l'empreinte mémoire de la BDD
            db_rows = dex.pool.getDatabaseHistoRowNb()
            db_heapmax = dex.pool.getDatabaseGlobalHeapMax()
            db_tbspace = dex.pool.getDatabaseHistoTablespace()
            db_recvmsgs = dex.pool.getCountRecvMsgOk()

            # -------------------------------------
            # Envoyer les données à l'affichage LCD
            # -------------------------------------
            info_edis = '{:2d}  {:7d}'.format(edis_intensite, edis_puissance)
            info_atm  = '{:6.2f} (hPa)'.format(env_atm)
            info_th   = '{:4.1f}  {:4.1f}'.format(env_temp, env_hum)
            info_dbtb = '{:6.2f}'.format(db_tbspace)
            info_dbhp = '{:6.2f}'.format(db_heapmax)
            info_sclk = sys_clock.strftime('%d/%m/%Y %H:%M')

            print('*' + info_edis + '*')
            print('*' + info_atm + '*')
            print('*' + info_th + '*')
            print('*' + info_dbtb + '*')
            print('*' + info_dbhp + '*')
            print('*' + info_sclk + '*')

            # Affichage des données de Téléinformation (page 0)
            if edis_ok:
                lcd.set_page(0, (LCD_MSG_HDR_IIPA, info_edis,
                                 LCD_MSG_HDR_TAR, edis_bareme))
            else:
                lcd.set_page(0, (LCD_MSG_HDR_IIPA, '--   --',
                                 LCD_MSG_HDR_TAR, '--'))

            # Affichage des données d'environnement (page 1)
            lcd.set_page(1, (LCD_MSG_HDR_PATM, info_atm,
                             LCD_MSG_HDR_TH, info_th))

            # Affichage de divers éléments (pages 2 et 3)
            # ("Rappel format {:,d} -> en entier + séparateur des milliers")
            lcd.set_page(2, (LCD_MSG_HDR_HOR, info_sclk))
            lcd.set_page(3, (LCD_MSG_HDR_TEL, '{:,d}'.format(db_recvmsgs), 'messages'))

            # Données de redémarrage du service (pages 4 et 5)
            restarted_nb = SystemInfoProvider.SystemInformation.get_service_restart_count(TELEINFO_SERVICE_UNIT_NAME)
            elapsed = SystemInfoProvider.SystemInformation.get_process_start_elapsed_time()
            uptime = SystemInfoProvider.SystemInformation.get_elapsed_time_since_bootup()

            lcd.set_page(4, (LCD_MSG_HDR_SVUP, str(elapsed.days) + 'j ' + str(elapsed.seconds) + 's',
                             LCD_MSG_HDR_REST, str(restarted_nb)))
            lcd.set_page(5, (LCD_MSG_HDR_SSUP, str(uptime.days) + 'j ' + str(uptime.seconds) + 's'))

            # Affichage des statistiques et des données remontées par la BDD (page 6 et 7)
            lcd.set_page(6, (LCD_MSG_HDR_DBTB, info_dbtb, LCD_MSG_HDR_DBHP, info_dbhp))
            lcd.set_page(7, (LCD_MSG_HDR_HIST, '{:,d}'.format(db_rows), 'lignes'))

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

            # --------------------------------------
            # Envoyer les données au bargraph 10xLED
            # --------------------------------------

            # Puissance remontée par la Téléinformation
            if edis_ok:
                StatusLeds.BargraphLeds.indication(leds, 0, 11000, edis_puissance)

            # ------------------------------
            # On se reverra dans 30 secondes
            # ------------------------------
            time.sleep(30)

        # En cas de souci, on quitte directement la boucle avant le prochain tour!
        # ------------------------------------------------------------------------
        except (Exception, KeyboardInterrupt, SystemExit) as e:
            print('>>> INTERRUPTED !', e)
            dex.pool.notifySystemFatalCondition()
            stop = True

        print('Has mainloop to STOP ?', stop)
    # ------------------------------------------ FIN DE LA BOUCLE PRINCIPALE -------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # Lorsqu'on quitte la boucle, c'est quand même une anomalie
    print('Main loop has terminated.')
    sys.exit(SYSEXIT_ERROR_INT)

# ------------------- Bloc de terminaison propre  ------------------
# ------------------------------------------------------------------
except (Exception, KeyboardInterrupt, SystemExit) as e:
    # C'est la séquence de fin!
    print('STOP! Doing cleanup sequence, then exit.', e)

    try:
        # Arrêt des mesures de l'environnement
        thp.close()
        print('[Monitoring released.]')
    except NameError:
        pass

    try:
        # Arrêt de la collecte Téléinfo ERDF
        ti.close()
        print('[Data collection released.]')
    except NameError:
        pass

    try:
        # Libération de la BDD
        dex.close()
        print('[Database closed.]')
    except NameError:
        pass

    try:
        # Message final sur l'écran LCD
        lcd.clear()
        lcd.set_page(0, ('******* STOP *******', 'PROGRAMME INTERROMPU'))
        print('[Final status set on LCD.]')

        # Libération de l'écran LCD
        lcd.close()
        print('[LCD subsystem released.]')
    except NameError:
        pass

    try:
        # Etat final : LED rouge allumée, toute seule
        # (programme interrompu)
        StatusLeds.BargraphLeds.indication(leds)
        StatusLeds.SystemLeds.aborted(leds)
        print('[Final status indication on leds.]')
    except NameError:
        pass

    print('ByeBye!')

    # On s'en va maintenant, on sort réellement si tous les autres threads sont terminés
    if type(e) is SystemExit:
        # On conserve le code de retour si on avait une demande de sortie
        raise e
    else:
        # Le code de retour signifiera 'interrompu'
        sys.exit(SYSEXIT_ERROR_INT)

    print('SHOULD NOT BE HERE.')
